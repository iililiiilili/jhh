import random

rankings = [
        [22, "삼성"],
        [2, "이성"],
        [20, "가성"],
        [18, "목성"]
    ]

name = input("이름을 입력하세요")

while True:
    print("\n[메뉴를 입력하세요]")
    i = int(input("1.게임시작  2.랭킹보기  3.게임종료  >>>  "))

    if i == 1:
        print("--> 게임을 시작합니다")
        print("컴퓨터가 숫자를 골랐습니다.")
        number = 0
        rand_num = int(random.randint(0,100))
        while True:
            i = int(input("(1~100) 숫자를 맞춰 보세요 >>>"))
            number += 1
            if i < rand_num:
                print("up")

            elif i > rand_num:
                print("down")
                    
            elif i == rand_num:
                print("정답입니다!")
                print("총시도 횟수 {}".format(number))
                break
            else :
                print("1부터 100까지 숫자만 적어주세요")
        rankings.append([number, name])

    elif i == 2:
        rankings.sort()
        print("--> 실시간 랭킹")
        for k in rankings:
            print(f"\n {k}", end=" ")
        print("\n")
            
    elif i == 3:
        print("-->게임을 종료합니다")
        break

    else :
        print("-->다시 입력해주세요")