from math import ceil
import math

"""
タクシーの運賃計算
    タクシーの運賃を計算するコードを作成せよ
    * 初乗り運賃は 1700m までは610円とする
    * 1700mを超えるとその後は 315m毎に 80円増えるものとする
    * 引数として走行距離(整数でm単位)が渡されるものとする
    * 戻り値は金額(整数値)とする
    * 1mでも超えれば80円単位でかかるものとする
    * 0mおよびマイナスの場合はNoneを返す
"""

def calc_account(m):
    # 実装は入れていません、自分で入れてください
    # 0mおよびマイナスの場合はNoneを返す
    if m <= 0 :
        return None
    # 初乗り運賃は 1700m までは610円とする
    # 1700mを超えるとその後は 315m毎に 80円増えるものとする
    if m <= 1700 :
        result = 610
    else :
        count = math.ceil((m - 1700) / 315)
        result = 610 + count * 80
    return result

if __name__ == "__main__":
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description="引数に金額を渡すとタクシー料金を計算します")
    parser.add_argument("distance", help="走行距離(メートル)", type=int)

    args = parser.parse_args()
    d = args.distance
    a = calc_account(d)
    if a == None:
        print("不正な数値です、1以上の整数値を渡してください", file=sys.stderr)
        sys.exit(1)
    print(f"走行距離 {args.distance}m => 金額は {calc_account(args.distance)}円です。")


