# simple-crawling-scraping-project
## project > youtube-crawling
### 목차
- 유튜브 content crawling
  * 제목, url, 조회수, 기간
  * csv로 저장
- 유튜브 subtitle crawling
  * 딕셔너리 파싱 -> txt로 저장
  
**주의! cromedriver가 본인 노트북에서 사용하는 crome과 버전이 맞아야함.**
```
#크롬 주소창에 입력
chrome://version/

```
```
#txt형식이 보기 불편하다면 엑셀로 다음과 같이 저장하세요
cur_df = pd.DataFrame(results)
cur_df.to_excel('저장할경로/스크립트.xlsx', index=False)

```
