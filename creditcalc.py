import math, argparse

def diff(prcpl, period, interest):
    pmt_sum = 0
    try:
        prcpl = float(prcpl)
        period = int(period)
        interest = float(interest) / 12 / 100
    except (ValueError, TypeError):
        print("Incorrect parameters")
    else:
        if all(x > 0 for x in (prcpl, period, interest)):
            for m in range(1, period + 1):
                monthly_pmt = math.ceil(prcpl / period + interest * \
                              (prcpl - prcpl * (m - 1) / period))
                print(f"Month {m}: payment is {monthly_pmt}")
                pmt_sum += monthly_pmt

            print(f"\nOverpayment = {pmt_sum - prcpl}")
        else:
            print("Incorrect parameters")
    return None

def nper(prcpl, payment, interest):
    try:
        prcpl = float(prcpl)
        payment = float(payment)
        interest = float(interest) / 12 / 100
    except (ValueError, TypeError):
        print("Incorrect parameters")
    else:
        if all(x > 0 for x in (prcpl, payment, interest)):
            period = math.ceil(math.log(payment / (payment - interest * prcpl), 1 + interest))
            year = period // 12
            year_text = ["", f"{year} year{'' if year == 1 else 's'}"]
            period_text = ["", f"{'' if year == 0 else ' and '}{period % 12} \
                month{'' if period % 12 == 1 else 's'}"]
            print(f'It will take {year_text[min(year, 1)]}{period_text[min(period % 12, 1)]} to repay this loan!')
            print(f"\nOverpayment = {math.ceil(period * payment - prcpl)}")
        else:
            print("Incorrect parameters")
    return None

def cal_prcpl(payment, period, interest):
    try:
        payment = float(payment)
        period = int(period)
        interest = float(interest) / 12 / 100
    except (ValueError, TypeError):
        print("Incorrect parameters")
    else:
        if all(x > 0 for x in (payment, period, interest)):
            prcpl = math.ceil(payment * (math.pow(1 + interest, period) - 1) /
                          (interest * math.pow(1 + interest, period)))
            print(f'Your loan principal = {prcpl}!')
            print(f"\nOverpayment = {period * payment - prcpl}")
        else:
            print("Incorrect parameters")
    return None

def pmt(prcpl, period, interest):
    try:
        prcpl = float(prcpl)
        period = int(period)
        interest = float(interest) / 12 / 100
    except (ValueError, TypeError):
        print("Incorrect parameters")
    else:
        if all(x > 0 for x in (prcpl, period, interest)):
            payment = prcpl * (interest * math.pow(1 + interest, period) / (math.pow(1 + interest, period) - 1))
            print(f"Your monthly payment = {math.ceil(payment)}!")
        else:
            print("Incorrect parameters")
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type")
    parser.add_argument("--payment")
    parser.add_argument("--principal")
    parser.add_argument("--periods")
    parser.add_argument("--interest")

    args = parser.parse_args()

    typ = args.type
    payment = args.payment
    prcpl = args.principal
    period = args.periods
    interest = args.interest

    if interest is None or typ not in [None, "annuity", "diff"]:
        print("Incorrect parameters")

    elif period is None and None not in (prcpl, payment) and typ == "annuity":
        nper(prcpl, payment, interest)
    elif prcpl is None and None not in (period, payment) and typ == "annuity":
        cal_prcpl(payment, period, interest)
    elif payment is None and None not in (prcpl, period) and typ == "annuity":
        pmt(prcpl, period, interest)
    elif payment is None and None not in (prcpl, period) and typ == "diff":
        diff(prcpl, period, interest)
    else:
        print("Incorrect parameters")

if __name__ == '__main__':
    main()
