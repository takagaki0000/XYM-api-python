# XYM-api-python

NEM２　　＞＞　XYMのapiをpython3で叩いて情報を得る小プログラム

部品

get_server     使えるサーバーからランダムに選ぶルーチンとサーバーの選び方

プログラム

address-infoget05.py  アドレスから　public-keyを表示する

getinfo_in_out_address_2.py  引数にaddressを与えると（-付きでOK）トランザクションを表示
　　　　　　　　　　　　　　　　　　　作成時点でpublic-keyが出ないので表示消している

get_node_info01.py   get_serverで使えるサーバーと書いてる各サーバーにランダムにアクセスして情報表示

get_info_own-server01.py  自分の建てたサーバーの情報　peerの情報は量が多いので１０秒待って最後に表示


随時追加する予定です
