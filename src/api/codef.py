import os
from easycodefpy import Codef
from dotenv import load_dotenv

load_dotenv()

demo_client_id = os.getenv('DEMO_CLIENT_ID')
demo_client_secret = os.getenv('DEMO_CLIENT_SECRET')

client_id = os.getenv('SANDBOX_CLIENT_ID')
client_secret = os.getenv('SANDBOX_CLIENT_SECRET')

public_key = os.getenv('PUBLIC_KEY')

# 코드에프 인스턴스 생성
codef = Codef()
codef.public_key = public_key

# 데모 클라이언트 정보 설정
# - 데모 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
# - 데모 서비스로 상품 조회 요청시 필수 입력 항목
codef.set_demo_client_info(demo_client_id, demo_client_secret)

# 정식 클라이언트 정보 설정
# - 정식 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
# - 정식 서비스로 상품 조회 요청시 필수 입력 항목
codef.set_client_info(client_id, client_secret)
