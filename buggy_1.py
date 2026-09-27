# -*- coding: utf-8 -*-
"""
buggy_1.py  ―  판매 데이터 매출 집계 (csv 모듈 버전)

dirty_sales.csv를 한 줄씩 읽어 '매출액 = 단가 x 수량'을 누적한다.
잘 돌아가는 것처럼 보이지만, 어떤 행에서 갑자기 멈춘다.

[과제] 이 스크립트를 실행해 Traceback을 얻고,
       진단 3단계 루틴(무엇이 / 어디서 / 왜)으로 원인을 특정한 뒤
       전처리로 해결하라. (힌트: 예외 타입은 무엇인가?)
"""
import csv

def calc_total(path):
    total = 0
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # 사전타입으로 데이터를 읽음.
        for i, row in enumerate(reader):
            # FIXED: price에 "5,200" 같은 천단위 콤마, "4200원" 같은 단위 문자,
            # 빈 문자열(결측)이 섞여 있어 int()가 바로 실패함(ValueError).
            # 콤마/원 제거 후 변환하고, 빈 값(결측)인 행은 집계에서 제외한다.
            price_str = row["price"].replace(",", "").replace("원", "").strip()
            if price_str == "":
                continue
            price = int(price_str)
            qty = int(row["quantity"])
            total += price * qty
    return total

if __name__ == "__main__":
    # FIXED: 존재하지 않는 "./Week4/dirty_sales.csv" 경로 -> 실제 파일 위치로 수정
    total = calc_total("dirty_sales.csv")
    print(f"총 매출액: {total:,}원")
