def solution(today, terms, privacies):
    # today = "2023.11.23"
    # terms = "A 6"
    # privacies[3] = 4번째(0부터 세니까) "2022.05.02 A"

    for userInfo in privacies:
        userInfoDate = userInfo[0: 9]
        print(userInfoDate)

    answer = []
    return answer