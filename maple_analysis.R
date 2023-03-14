# 데이터 불러오기
maple <- read.csv('maple.csv')
maple <- maple[,2:4]

# ------------- prob: 확률 조작 전 후의 상황 (범주형 변수)
# 메이플 확률 조작 이전: 0
# 메이플 확률 조작 이후: 1
maple[maple$prob == '1']
maple[maple$prob == '0']

# EDA (히스토 그램)
hist(maple[which(maple$prob == '1'),]$rank,
     xlim = c(4,10),
     col = adjustcolor(col ='red',alpha = 0.1),
     border = 'red',
     main = '메이플스토리 순위 히스토그램 (2020.08 ~ 2021.09)',
     xlab = 'rank')
hist(maple[which(maple$prob == '0'),]$rank,
     col = adjustcolor(col ='blue',alpha = 0.1),
     add = T,
     border = 'blue')
legend("topright",legend=c("균일화 패치 전","균일화 패치 후"),fill=c(adjustcolor(col ='blue',alpha = 0.1),adjustcolor(col ='red',alpha = 0.1)))

# EDA (Box Plot)

boxplot(rank ~ prob,data = maple,xlab='',col = c(adjustcolor(col ='blue',alpha = 0.1),adjustcolor(col ='red',alpha = 0.1)),main = '메이플스토리 순위 박스플랏 (2020.08 ~ 2021.09)')
legend("topright",legend=c("균일화 패치 전","균일화 패치 후"),fill=c(adjustcolor(col ='blue',alpha = 0.1),adjustcolor(col ='red',alpha = 0.1)))

# 확률 조작 전 후 정규성 검정
shapiro.test(maple[which(maple$prob == '1'),]$rank)
shapiro.test(maple[which(maple$prob == '0'),]$rank)

# 정규성을 만족하지 못하므로 t-test 대신 wilcox 분석 진행
wilcox.test(rank ~ prob,data = maple)