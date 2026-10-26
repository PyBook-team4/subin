def signup_id():
    """
    회원가입시 아이디를 입력받아 반환하는 함수입니다.
    """

    while True:
        user_id = input("아이디(이메일)를 입력하세요: ").strip()

        if "@" in user_id:  #아이디가 이메일인지 확인
            break
        else:
            print("이메일 형식이 아닙니다. 다시 아이디를 입력해주세요.")

    return user_id

def signup_password():  
    """
    회원가입시 비밀번호를 입력받아 반환하는 함수입니다.
    """

    special_chars = "!@#$%^&*()_+-=[]|;:',./<>?" # 특수문자 포함 확인용 문자열

    while True:
        user_password = input("비밀번호를 입력하세요: ")

        if len(user_password) < 8: # 비밀번호가 8글자 이상인지 확인
            print("비밀번호는 8글자 이상으로 입력해주세요.")

        elif not any(char in special_chars for char in user_password): #비밀번호에 특수문자가 포함되었는지 확인
            print("특수문자가 최소 1개 이상 포함되도록 설정해주세요.")

        else:
            break

    return user_password

def signup_name():
    """
    회원가입시 이름을 입력받아 반환하는 함수입니다.
    """
    user_name = input("성함을 입력해주세요: ").strip()

    return user_name

def signup_phone():
    """
    회원가입시 전화번호를 입력받아 반환하는 함수입니다.
    """
    
    while True:
        user_phone = input("연락처를 입력해주세요: ")

        # 사용자가 하이픈(-)을 포함하여 입력해도 제거하기 위한 변수
        cleaned_phone = user_phone.replace("-", "").replace(" ", "")

        # 연락처가 올바르게 입력되었는지 확인: 11자리인지, 번호로만 구성되었는지, 010으로 시작했는지
        if len(cleaned_phone) == 11 and cleaned_phone.isdigit() and cleaned_phone.startswith("010"):

            user_phone = cleaned_phone 
            break

        else:
            print("잘못된 형식입니다. 올바른 연락처를 다시 입력해주세요.")

    return user_phone


def signup_find_password():
    """
    회원가입시 비밀번호 찾기용 질문을 선택하고 답을 입력받아 반환하는 함수입니다.
    """
    find_password_questions = [
        "내가 생각하는 나만의 보물1호는?",
        "졸업한 초등학교의 이름은?",
        "가장 감명 깊게 본 영화의 제목은?",
        "조부모님의 성함은?",
        "생애 첫 아르바이트를 했던 가게의 이름은?",
        "가장 처음으로 키웠던 반려동물의 이름은?",
        "태어나서 처음 살았던 동네의 이름은?"] # 비밀번호 찾기용 질문 목록들

    for number, question in enumerate(find_password_questions, start=1):
        print(f"{number}. {question}")
    
    while True:
        choice = input("비밀번호를 찾을 때 질문을 선택하세요(번호 입력): ").strip()

        #숫자를 입력했는지 확인
        if not choice.isdigit():
            print("숫자만 입력해주세요.")
            continue

        choice_num = int(choice)

        # 선택지 중의 숫자를 입력했는지 확인
        if choice_num < 1 or choice_num > len(find_password_questions):
            print(f"1 ~ {len(find_password_questions)} 의 번호를 입력하여 선택해주세요.")
        else:
            selected_question = find_password_questions[choice_num-1]
            break


    user_answer = input("선택하신 질문의 답을 입력하세요: ").strip()

    return {
        "question" : selected_question,
        "answer" : user_answer
    }

def signup_interests():
    """
    회원가입시 책 관심분야를 설정하고 반환하는 함수입니다.
    """

    available_categories = [
    "총류", "철학", "종교", 
    "사회과학", "자연과학", "기술과학", "예술", 
    "언어", "문학", "역사"
    ] # 국립중앙도서관 도서관 정보나루의 주제 분류를 참고
    
    user_categories = []

    # 선택할 수 있는 관심분야 항목 출력
    for number, category in enumerate(available_categories, start=1):
        print(f"{number}. {category}")

    while len(user_categories) < 3:
        choice = input(f"\n관심분야 번호 입력 ({len(user_categories)}/3) (종료는 엔터): ").strip()

        # 사용자가 1~2개만 선택하고 싶을 때, 엔터를 치면 즉시 종료
        if not choice:
            break
        
        # 입력한 값이 숫자인지 먼저 확인
        if not choice.isdigit():
            print("숫자만 입력해주세요.")
            continue

        # 입력받은 번호를 정수형으로 전환
        choice_num = int(choice)
    
        # 입력한 숫자가 1번부터 목록의 마지막 번호 사이에 있는지 확인
        if choice_num < 1 or choice_num > len(available_categories):
            print("목록에 없는 번호입니다.")
            continue
        
        # 사용자가 입력한 번호를 분류명으로 변환
        selected_category = available_categories[choice_num - 1]

        # 이미 관심분야에 추가한 항목인지 중복 검사
        if selected_category in user_categories:
            print("이미 선택한 항목입니다.")
            continue

        # 회원 관심분야에 추가
        user_categories.append(selected_category)
        print(f"-> '{selected_category}' 항목이 추가되었습니다.")

    print(f"\n최종 설정된 관심분야: {user_categories}")

    return user_categories

def create_user_profile():
    """
    모든 회원가입 함수를 순서대로 실행하고,
    결과를 딕셔너리 하나로 모아서 반환하는 통합 함수입니다.
    """
    print("\n=== 회원가입을 시작합니다 ===")
    
    user_profile = {
        "user_id": signup_id(),
        "password": signup_password(),
        "name": signup_name(),
        "phone": signup_phone(),
        "find_password": signup_find_password(),
        "interests": signup_interests()
    }
    
    print(f"\n=== {user_profile['name']}님, 회원가입이 완료되었습니다! ===")
    return user_profile


    


