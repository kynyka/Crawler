### 緣起
某人要從某站扒點圖下來，於是硬著頭皮寫了個粗糙的爬蟲 \_(:qゝ∠)\_
### 碎語
當然採集時遇到了點問題，就是有時下著下著就不動了。`IOError: [Errno socket error] [Errno 10060]`以及`IOError: ('http protocol error', 0, 'got a bad status line', None)`。查而複查，某言 "频繁的访问某个网站会被认为是DOS攻击，通常做了Rate-limit的网站都会停止响应一段时间..."，於是加sleep；某言可能user-agent啥的做了限制，於是試著給urllib加user-agent[^ua]（Py3裡更便捷）；也擔憂過是否下載內容過小而去遞歸調用... 不過貌似還真是網站做的限制，在不同時間陸續將幾個目錄的圖片下下來了。有的目錄會少一兩張，不過妙的是有個目錄九千六百多張圖，給我下下來九千七百多張（我在圖的名稱前附加了序號）；檢視一番，發現有的排前面的圖，會在之後以一個比正常序號靠后的數字[^num]加圖片名重新出現在文件夾裡 (̿▀̿̿Ĺ̯̿̿▀̿ ̿)̄，有的圖則會以一個比正常序號靠前的數字加圖片名的形式重現。嘛，這樣至少可以說主因就是網站了。
從零學寫以來，查了些東西，弄清了些東西，得到了些東西，終得個不算徒勞吧。這破程序沒搞多線程之類的，天曉得咱會不會給添上。

[無聊的附圖·其一](http://i.imgur.com/SGyGHs9.jpg)
[無聊的附圖·其二](http://i.imgur.com/Yq43Bad.jpg)

[^ua]: questions/19922419 & 2364593，不禁莞爾，絕非莫逆。
[^num]: 不論靠前還是靠後，數字上倒都是只是偏移了一兩個而已。