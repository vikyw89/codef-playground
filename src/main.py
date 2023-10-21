import json
from easycodefpy import API_DOMAIN, ServiceType, encrypt_rsa, encode_to_file_string
from api.codef import *

def get_connected_id(service_type=ServiceType.SANDBOX,
                     user_Data={
                         ""
                     }):
    # TODO: get connection id, if none exist, create one
    connected_id_list = json.loads(codef.get_connected_id_list(service_type, None))['data']['connectedIdList']

    if len(connected_id_list) == 0:
        res = codef.create_account(service_type,)

account_list = []
account = {
    'countryCode':  'KR',
    'businessType': 'BK',
    'clientType':   'P',
    'organization': '0004',
    'loginType':    '1',
    'id':           "nobody",
}

# 비밀번호 설정
pwd = encrypt_rsa("password", codef.public_key)
account['password'] = pwd
account_list.append(account)

parameter = {
    'accountList': account_list,
}

codef.token
codef.create_account(ServiceType.SANDBOX, parameter)
# 요청
res = codef.get_connected_id_list(ServiceType.SANDBOX, None)
print(len(json.loads(res)['data']['connectedIdList']))

def get_user_account_held(service_type=ServiceType.SANDBOX):
    res = codef.request_product(
        "/v1/kr/bank/p/account/account-list",
        service_type,
        {
            "organization": "0020",
            "connectedId": "3Lj7J-OvQ",
            "birthDate": "",
            "withdrawAccountNo": "",
            "withdrawAccountPassword": ""
        }
    )
    return res

def get_user_saving_banks(service_type=ServiceType.SANDBOX):
    # https://developer.codef.io/products/bank2/common/p/account
    res = codef.request_product(
        "/v1/kr/bank2/p/account/account-list",
        service_type,
        {
            "organization": "0020",
            "connectedId": "3Lj7J-OvQ",
            "bankName": "sky"
        }
    )
def get_banking_transaction_history(service_type=ServiceType.SANDBOX):
    # https://developer.codef.io/products/bank/common/p/transaction
    bank_transaction = codef.request_product(
        "/v1/kr/bank/p/account/transaction-list",
        service_type,
        {
            "organization": "0020",
            "connectedId": "3Lj7J-OvQub96etCy.0xZz",
            "account": "1002440000000",
            "startDate": "20190601",
            "endDate": "20190619",
            "orderBy": "0",
            "inquiryType": "1",
            "accountPassword": "RSA암호화된 비밀번호",
            "birthDate": "",
            "withdrawAccountNo": "",
            "withdrawAccountPassword": "RSA암호화된 비밀번호"
        }
    )
    print(bank_transaction)
    # https://developer.codef.io/products/bank/common/p/installmentSavings
    saving_bank_transaction = codef.request_product(
        "/v1/kr/bank/p/account/transaction-list",
        service_type,
        {
            "organization": "0020",
            "connectedId": "3Lj7J-OvQub96etCy.0xZz",
            "account": "1002440000000",
            "startDate": "20190601",
            "endDate": "20190619",
            "orderBy": "0",
            "inquiryType": "1",
            "accountPassword": "RSA암호화된 비밀번호",
            "birthDate": "",
            "withdrawAccountNo": "",
            "withdrawAccountPassword": "RSA암호화된 비밀번호"
        }
    )
    print(saving_bank_transaction)
    # /v1/kr/bank/p/loan/transaction-list
    loan_transaction_history = codef.request_product(
        "/v1/kr/bank/p/loan/transaction-list",
        service_type,
        {
            "organization": "0020",
            "connectedId": "3Lj7J-OvQub96etCy.0xZz",
            "account": "1002440000000",
            "startDate": "20190601",
            "endDate": "20190619",
            "orderBy": "0",
            "inquiryType": "1",
            "accountLoanExecNo": "",
            "birthDate": "",
            "withdrawAccountNo": "",
            "withdrawAccountPassword": "RSA암호화된 비밀번호"
        }
    )