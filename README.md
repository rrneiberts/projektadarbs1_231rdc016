# projektadarbs1_231rdc016
Projekta darbs kursam "Lietujomprogrammatūras automatizēšanas rīki"


Saite uz video: https://www.youtube.com/watch?v=66_R1F2gN3s

Šis projekts ir programma, kas meklē cilvēku vārda dienas. Programmu palaižot, terminālī tiek izprintētas šodienas vārdiem vārda dienas. Lai ievadītu vēlamo vārdu terminālī un uzsāktu meklēšanu ir jāuzgaida līdz parādās "Lūdzu ievadiet vārdu: ". Ievadot vārdu un uzspiežot "ENTER" tiek meklēts kad vārdam ir vārda diena. Pēc programmas apstrādes terminālī tiek izvadīts datums, kurā šim vārdam ir vārda diena, citi vārdi, kuriem ir vārda diena tajā datumā, dažkārt arī tiek izvadītas nozīmes un vēsturiski raksti par vārdiem, kā arī kalendārā nerakstītie vārdi, kas svin vārda dienu tajā datumā. Lai meklētu jaunu vārdu, programma ir jāpalaiž no jauna. 


Projekta izveidošanā izmantoju bibliotēkas kā Beautiful soup 4, requests, Selenium, time, kuras ir ņemtas no ceturtās un piektās lekcijas par tīmekļa skrāpēšanu un tīmekļa programmatūras automatizēšanu. 

No bs4 bibliotēkas izmantoju teksta funkcijas kā find_all, lai iegūtu tekstu no pārlūka un saglabātu to mainīgajā. Requests un bs4 apvienoju, lai izmantotu funkcijas kā "html_parser", lai nolasītu visu mājaslapas saturu. Requests bibliotēka noderēja, lai izveidotu savienojumu ar mājaslapas "https://www.1188.lv/varda-dienas" serveri un pārliecinātos, ka serveris strādā un turpmākās darbības ir iespējamas. Pārlūks tiek atvērts noklusējuma režīmā, tādejādi netiek ietekmēta programmas kvalitāte. Bs4 bibliotēku izmantoju, lai iegūtu arī specifickus teksta lauciņus, kad Selenium bibliotēka nespēja to izdarīt. 

No Selenium bibliotēkas (webdriver, Service, By, Keys) izmantoju automatizēšanas rīkus, lai automātiski palaižot programmu tiktu veiktas darbības, kas mijiedarbojas ar mājaslapas pogām, teksta kastēm un arī teksta iegūsānu, glabāsānu. Lai mijiedarbotos ar mājaslapas funkcijām izmantoju funkcijas kā click(), send_keys, Keys.ENTER, lai automātiski apstiprinātu sīkdatnes, ievadītu vārdu un nospiestu "ENTER", mainot pārlūka url adresi un iegūstot vajadzīgos datus nākamajā pārlūka adresē.
Projekta kodā ir iekļauti loģiskie operatori un cikli, kas pārveido iegūto tekstu no pārlūka, ievieto tos masīvos un ar citu ciklu palīdzību spēj apstrādāt masīva elementus, lai izveidotu fināla izvadi terminālī, kas ir cilvēkam izlasāms.



Kļūdas tiek pārbaudītas caur loģisko operatoru, salīdzinot oriģinālo url ar jauno url, kuru iegūst pēc vārda ievades terminālī. Ja vārds tiek atrast pārlūkā, tad url mainās un kamēr tie nav vienādi ar iepriekšējo url tad notiek tālākas programmas darbības. Pretējā gadījumā url varētu nemainīties dažādu iemeslu dēļ, piemēram, retos gadījumos izlec reklāma, kāda no koda funkcijām nenostrādāja, lēna apstrāde (lēns internets, pārslogots dators), vārds tika uzrakstīts nepareizi vai netika atrasts vispār. Atkārtota ievades prasība notiks, ja ievadē tika iekļauti skaitļi vai jebkādi citi simboli.


