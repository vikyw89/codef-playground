from easycodefpy import API_DOMAIN, ServiceType, encrypt_rsa, encode_to_file_string
from api.codef import *

# parameter = {
#     'connectedId': '8PQI4dQ......hKLhTnZ',
#     'organization': '0004',
# }

# # DEMO
# # 코드에프 정보 조회 요청
# # - 서비스타입(0:정식, 1:데모, 2:샌드박스)
# # 개인 보유계좌 조회 (https://developer.codef.io/products/bank/common/p/account)
# product_url = "/v1/kr/bank/p/account/account-list"
# res = codef.request_product(product_url, ServiceType.SANDBOX, parameter)
# print(res)

# res = codef.get_connected_id_list(ServiceType.SANDBOX, None)
# print(res)


# GET CONNECTID


# # CREATE ACCOUNT
# # 요청 파라미터 설정
# # - 계정관리 파라미터를 설정(https://developer.codef.io/cert/account/cid-overview)
# account_list = []
# account = {
#     'countryCode':  'KR',
#     'businessType': 'BK',
#     'clientType':   'P',
#     'organization': '0004',
#     'loginType':    '1',
#     'id':           "user_id",
# }

# # 비밀번호 설정
# pwd = encrypt_rsa("password", codef.public_key)
# account['password'] = pwd
# account_list.append(account)

# parameter = {
#     'accountList': account_list,
# }

# # 요청
# res = codef.create_account(ServiceType.SANDBOX, parameter)
# print(res)

# # ADD ACCOUNT
# # 요청 파라미터 설정
# # - 계정관리 파라미터를 설정(https://developer.codef.io/cert/account/cid-overview)
# account_list = []
# account = {
#     'countryCode':  'KR',
#     'businessType': 'BK',
#     'clientType':   'P',
#     'organization': '0004',
#     'loginType':    '0',
# }

# # 비밀번호 설정
# pwd = encrypt_rsa("password", codef.public_key)
# account['password'] = pwd
# account_list.append(account)

# # 인증서 정보 가져오기
# cert = encode_to_file_string('CERT_FILE_PATH')
# key = encode_to_file_string('KEY_FILE_PATH')
# account['derFile'] = cert
# account['keyFile'] = key

# parameter = {
#     'accountList': account_list,
#     'connectedId': '8PQI4dQ......hKLhTnZ',
# }

# # 요청
# res = codef.add_account(ServiceType.SANDBOX, parameter)
# print(res)

# # GET ACCOUNT LIST
# # 파라미터 설정
# parameter = {
#     'connectedId': '8PQI4dQ......hKLhTnZ',
# }

# # 요청
# res = codef.get_account_list(ServiceType.SANDBOX, parameter)
# print(res)

# # TRANSACTION LIST
# parameter = {
#     "organization": "0020",
#     "connectedId": "3Lj7J-OvQub96etCy.0xZz",
#     "account": "1002440000000",
#     "startDate": "20190601",
#     "endDate": "20190619",
#     "orderBy": "0",
#     "inquiryType": "1",
#     "accountPassword": "RSA암호화된 비밀번호",
#     "birthDate": "",
#     "withdrawAccountNo": "",
#     "withdrawAccountPassword": "RSA암호화된 비밀번호"
# }

# # https://developer.codef.io/products/bank2/common/p/transaction
# product_url = "/v1/kr/bank/p/account/transaction-list"
# res = codef.request_product(product_url, ServiceType.SANDBOX, parameter)
# print(res)

# CARD
parameter = {
    "organization": "0309",
    "connectedId": "3Lj7J-OvQ",
    "birthDate": "",
    "cardNo": "",
    "cardPassword": ""
}


# https://developer.codef.io/products/bank2/common/p/transaction
product_url = "/v1/kr/card/p/account/result-check-list"
res = codef.request_product(product_url, ServiceType.SANDBOX, parameter)
print(res)
