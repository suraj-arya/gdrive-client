import unittest
from gdrive import GDriveClient

GDRIVE_CLIENT_EMAIL = ''
GDRIVE_ROOT_FOLDER_ID = ''
GDRIVE_PRIVATE_KEY = ""


class TestGdriveClient(unittest.TestCase):

    def test_create_folder(self):
        client = GDriveClient(GDRIVE_CLIENT_EMAIL, GDRIVE_PRIVATE_KEY)
        print client.get_or_create_folder('test_folder',
                                          GDRIVE_ROOT_FOLDER_ID)


if __name__ == '__main__':
    unittest.main()