# niten
Share Nice Item.

Nice Item -> nitem -> niten -> 910


## Idea
- 貼文以物品為主。
- 以房間(Room)做區隔，一個使用者可以加入多個房間，一個房間也可以被多個使用者加入。
  - 房間為私人，需設定密碼。
  - 密碼透過from django.contrib.auth.hashers import make_password, check_password進行加密及檢查。
  - 房間最高權限: 房間建立者、開發者

- 房間、使用者、貼文執行刪除後先將is_archived設為True，過n天再刪除。
- Post沒有likes, likes是毒藥。
- 使用者可建立房間。
- 該如何加入房間？
  - 透過搜尋

## Algorithm
- Servey 物件偵測API，看要將圖片存在本地還是imgur，再做物件判斷
- 含有物品則會獲得較高的喜好度
- 