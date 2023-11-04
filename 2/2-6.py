def cnt_spanish_alphabets(string):
    allowed_input = set('abcdefghijklmnopqrstuvwxyz.,~')
    if not set(string).issubset(allowed_input):
        raise ValueError("알파벳 소문자, '.', ',', '~'만 입력 가능합니다.")
        # 허용 가능한 알파벳 소문자, '.', ',', '~' 가 아닌 다른 문자가 들어가면 ValueError가 발생하게 했음.
    
    spanish_pronunciation = {
        'a,': 'á',
        'e,': 'é',
        'i,': 'í',
        'n~': 'ñ',
        'o,': 'ó',
        'u,': 'ú',
        'u..': 'ü'}
    # 스페인 알파벳 목록
    
    for key, value in spanish_pronunciation.items():
        string = string.replace(key, value)
    #입력한 문자열 내의 스페인 알파벳이 변경된 형태로 입력되게 함.
    
    print(len(string))
    #몇 개의 스페인 알파벳으로 이루어져 있는지 출력
    #함수 끝
    
cnt_spanish_alphabets("espan~afu,tbol")  #함수 테스트 코드
cnt_spanish_alphabets("si,aqui,esta,")   #함수 테스트 코드