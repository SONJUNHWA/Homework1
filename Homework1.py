def calculate_dividend(dividend_yield, number_of_shares, share_price):
    # 배당률을 소수점으로 변환
    dividend_yield_decimal = dividend_yield / 100
    # 배당금 계산
    dividend = dividend_yield_decimal * number_of_shares * share_price
    return dividend


def main():
    while True:
        print("\n배당금 계산기 프로그램")
        print("1. 배당금 계산")
        print("2. 종료")

        choice = input("원하는 기능을 선택하세요 (1/2): ")

        if choice == '1':
            try:
                dividend_yield = float(input("배당률을 입력하세요 (예: 5는 5%를 의미): "))
                number_of_shares = int(input("주식 수를 입력하세요: "))
                share_price = float(input("주식 가격을 입력하세요: "))
                if dividend_yield < 0 or number_of_shares < 0 or share_price < 0:
                    print("모든 입력 값은 양수이어야 합니다. 다시 시도하세요.")
                    continue
                result = calculate_dividend(dividend_yield, number_of_shares, share_price)
                print(f"예상 배당금: {result:.2f} 원")
            except ValueError:
                print("올바른 숫자를 입력하세요.")

        elif choice == '2':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택하세요.")


if __name__ == "__main__":
    main()
