import pandas as pd

def 정제(df):
	정제본 = df.copy()

	# 점수가 비어 있는 행을 삭제한다.
	정제본 = 정제본.dropna(subset=["점수"])
	print(f"점수 결측 행 삭제 후: {len(정제본)}행")

	# 모든 열이 같은 중복 행을 하나만 남긴다.
	정제본 = 정제본.drop_duplicates()
	print(f"중복 행 삭제 후: {len(정제본)}행")

	# 반과 과목 값의 앞뒤 공백을 제거한다.
	정제본["반"] = 정제본["반"].str.strip()
	정제본["과목"] = 정제본["과목"].str.strip()
	print(f"공백 제거 후: {len(정제본)}행")

	# 점수가 0 이상 100 이하인 행만 남긴다.
	정제본 = 정제본[정제본["점수"].between(0, 100)].copy()
	정제본["점수"] = 정제본["점수"].astype(int)
	print(f"점수 범위 정리 후: {len(정제본)}행")

	return 정제본


import pandas as pd
df = pd.read_csv("mini.csv") 
df = 정제(df)
print(sorted(df["반"].unique())) # ['1반', '2반']       ← 세 개에서 두 개로
print(sorted(df["과목"].unique())) # ['수학','영어','프로그래밍'] ← 네 개에서 세 개로



df = pd.read_csv("mini.csv") 

print(df.shape) # (114, 5)
print(df["점수"].isna().sum())        # 6      ← 빈 칸이 몇 개인가
print(df.duplicated().sum())         # 4      ← 완전히 같은 행이 몇 개인가
print(df["반"].unique())             # ['2반' '1반' '1반 ']      ← 세 개?
print(df["과목"].unique())           # ['수학' '프로그래밍' '영어' '프로그래밍 ']
print(df["점수"].describe())         # max 999.0  min -5.0   ← 점수인데?


# ...existing code...

df = 정제(df)
수학_df = df[df["과목"] == "수학"].copy()
print(f"수학 과목 행 수: {len(수학_df)}")

# ...existing code...

print("\n반별 점수 평균:")
print(df.groupby("반")["점수"].mean())

print("\n과목·반별 점수 평균:")
print(df.groupby(["과목", "반"])["점수"].mean())

# ...existing code...

반별_통계 = (
    df.groupby("반")
    .agg(
        개수=("점수", "count"),
        평균=("점수", "mean"),
        중앙값=("점수", "median"),
        최댓값=("점수", "max"),
    )
    .round(2)
)

print("\n반별 점수 통계:")
print(반별_통계)

# ...existing code...

반별_합계 = df.groupby("반")["점수"].sum()
전체_합계 = df["점수"].sum()

print("\n[합계 일치 확인]")
print(반별_합계)
print("반별 합계의 합:", 반별_합계.sum())
print("전체 점수 합:", 전체_합계)
print("합계 일치:", 반별_합계.sum() == 전체_합계)