from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
from django.conf import settings


class FDFSStorage(Storage):
    """
      fast dfs 文件存储类
    """

    def __init__(self, client_conf=None, base_url=None):
        """
          初始化
        :param client_conf:
        :param base_url:
        """
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf
        if base_url is None:
            base_url = settings.FDFS_URL
        self.base_url = base_url

    def _open(self, name, mode='rb'):
        ''' 打开文件时使用 '''
        pass

    def _save(self, name, content):
        """
          保存文件时使用
        :param name: 你选择上传文件的名字
        :param content: 包含你上传文件内容的 File 对象
        :return:
        """

        # 创建一个 Fdfs_client 对象
        client = Fdfs_client(self.client_conf)

        # 上传文件到 fast_dfs 系统中
        res = client.upload_by_buffer(content.read())

        # dict
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # }

        if res.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传到 Fast_dfs 失败！')

        # 获取返回的文件 ID
        filename = res.get('Remote file_id')

        return filename

    def exists(self, name):
        """
          Django 文件名是否可用
        :param name:
        :return:
        """
        return False

    def url(self, name):
        """
         Django 判断 文件名是否可用
         作用： 返回前端image url
        :param name:
        :return:
        """
        return self.base_url + name
