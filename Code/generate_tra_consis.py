import numpy as np
import pandas as pd

def make_tra():
    df = pd.read_excel('constituents-financials.xlsx')
    data = df.values
    df = pd.read_excel('top_company.xlsx')
    top = df.values
    print(top)
    test_list = np.load("earnings_call_3days.npy")
    for i in test_list:
        for j in data:
            if j[1] == i[2]:
                sector = j[2]
                break
        for j in top:
            if j[0] == sector:
                top_c = j[1]
                top_c_ = j[2]
                if j[1] == i[2]:
                    top_c = j[2]
                    top_c_ = j[3]
        text = i[3].replace(top_c,top_c_).lower().replace(' we ',' '+top_c+' ').replace(' our ',' '+top_c+"'s ").lower()
        i[3] = text
    print(len(test_list))
    np.save("tra_earnings_call_3days.npy", test_list)


if __name__ == "__main__":
    make_tra()