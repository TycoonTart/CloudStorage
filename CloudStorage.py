from posixpath import relpath
import dropbox
import os
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for fileName in files:
                local_path=os.path.join(root,fileName)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)

                with open(file_from,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

        
def main():
    access_token='sl.A5JNv_5F2qWnSumtxAF0uXwacLWsKc7DvGOEJRcrTo-auXvVVVCy5lyYwOjLz_PaaLS9hShAISLStteyTU0YZEEDK3ZCGLnJ5eLvrhm3-2xr11LpTLCcS64KYk1E7ZoSYHcjXnE'
    transferData=TransferData(access_token)
    file_from=input("enter file path to transfer:")
    file_to=input("enter the full path to upload to dropbox:")
    transferData.upload_file(file_from,file_to)
    print("files has been moved")
main()

