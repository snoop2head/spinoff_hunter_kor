# Spinoff Hunter Korean ver

한국 상장 회사 중 인적 분할 소식 구독
* 뉴스 출처: [The Bell](http://www.thebell.co.kr/free/content/Search.asp?keyword=%EC%9D%B8%EC%A0%81%EB%B6%84%ED%95%A0)
* 재무 정보 출처: [QuantKing csv file](http://www.quantking.co.kr/page/charge.php?boardid=JS_board_charge&mode=list)

## 프로젝트 목적
* 퀀트킹데이터 엑셀파일을 repository에 push할 때마다, 인적분할 소식이 있는 회사들의 재무 정보를 하나의 csv 파일로 뽑아내려는 것.
* 인적분할 소식이 있는 회사들의 재무 정보는 [_spinoff_data](./_spinoff_data)에 위치.

### How to Run
* Step 1. 
Download Quantking excel data [from website](http://www.quantking.co.kr/page/charge.php?boardid=JS_board_charge&mode=list) and move the file to [finance_data_xlsx](./finance_data_xlsx)

* Step 2. Run main.py
```shell
python main.py
```


### To Do

- [x] Get the most recent file
- [x] Upload csv file to Google Spreadsheet since csv -> xlsx doesn't support Korean language 😭

