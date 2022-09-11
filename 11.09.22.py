# noinspection PyUnresolvedReferences
from flask import Flask
# noinspection PyUnresolvedReferences
from flask import render_template
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)


@app.route('/Петя')
def petya():
    text = """
    ГЛАВА ПЕРВАЯ
И жить торопится, и чувствовать спешит.
Кн. Вяземский.

I
«Мой дядя самых честных правил,
Когда не в шутку занемог,
Он уважать себя заставил
И лучше выдумать не мог.
Его пример другим наука;
Но, боже мой, какая скука
С больным сидеть и день и ночь,
Не отходя ни шагу прочь!
Какое низкое коварство
Полуживого забавлять,
Ему подушки поправлять,
Печально подносить лекарство,
Вздыхать и думать про себя:
Когда же черт возьмет тебя!»
II
Так думал молодой повеса,
Летя в пыли на почтовых,
Всевышней волею Зевеса
Наследник всех своих родных.
Друзья Людмилы и Руслана!
С героем моего романа
Без предисловий, сей же час
Позвольте познакомить вас:
Онегин, добрый мой приятель,
Родился на брегах Невы,
Где, может быть, родились вы
Или блистали, мой читатель;
Там некогда гулял и я:
Но вреден север для меня 1.
III
Служив отлично благородно,
Долгами жил его отец,
Давал три бала ежегодно
И промотался наконец.
Судьба Евгения хранила:
Сперва Madame за ним ходила,
Потом Monsieur ее сменил.
Ребенок был резов, но мил.
Monsieur l'Abbé, француз убогой,
Чтоб не измучилось дитя,
Учил его всему шутя,
Не докучал моралью строгой,
Слегка за шалости бранил
И в Летний сад гулять водил.
IV
Когда же юности мятежной
Пришла Евгению пора,
Пора надежд и грусти нежной,
Monsieur прогнали со двора.
Вот мой Онегин на свободе;
Острижен по последней моде,
Как dandy 2 лондонский одет —
И наконец увидел свет.
Он по-французски совершенно
Мог изъясняться и писал;
Легко мазурку танцевал
И кланялся непринужденно;
Чего ж вам больше? Свет решил,
Что он умен и очень мил.
V
Мы все учились понемногу
Чему-нибудь и как-нибудь,
Так воспитаньем, слава богу,
У нас немудрено блеснуть.
Онегин был по мненью многих
(Судей решительных и строгих)
Ученый малый, но педант:
Имел он счастливый талант
Без принужденья в разговоре
Коснуться до всего слегка,
С ученым видом знатока
Хранить молчанье в важном споре
И возбуждать улыбку дам
Огнем нежданных эпиграмм.
VI
Латынь из моды вышла ныне:
Так, если правду вам сказать,
Он знал довольно по-латыне,
Чтоб эпиграфы разбирать,
Потолковать об Ювенале,
В конце письма поставить vale,
Да помнил, хоть не без греха,
Из Энеиды два стиха.
Он рыться не имел охоты
В хронологической пыли
Бытописания земли:
Но дней минувших анекдоты
От Ромула до наших дней
Хранил он в памяти своей.
VII
Высокой страсти не имея
Для звуков жизни не щадить,
Не мог он ямба от хорея,
Как мы ни бились, отличить.
Бранил Гомера, Феокрита;
Зато читал Адама Смита
И был глубокой эконом,
То есть умел судить о том,
Как государство богатеет,
И чем живет, и почему
Не нужно золота ему,
Когда простой продукт имеет.
Отец понять его не мог
И земли отдавал в залог.
VIII
Всего, что знал еще Евгений,
Пересказать мне недосуг;
Но в чем он истинный был гений,
Что знал он тверже всех наук,
Что было для него измлада
И труд, и мука, и отрада,
Что занимало целый день
Его тоскующую лень, —
Была наука страсти нежной,
Которую воспел Назон,
За что страдальцем кончил он
Свой век блестящий и мятежный
В Молдавии, в глуши степей,
Вдали Италии своей.
IX

X
Как рано мог он лицемерить,
Таить надежду, ревновать,
Разуверять, заставить верить,
Казаться мрачным, изнывать,
Являться гордым и послушным,
Внимательным иль равнодушным!
Как томно был он молчалив,
Как пламенно красноречив,
В сердечных письмах как небрежен!
Одним дыша, одно любя,
Как он умел забыть себя!
Как взор его был быстр и нежен,
Стыдлив и дерзок, а порой
Блистал послушною слезой!
XI
Как он умел казаться новым,
Шутя невинность изумлять,
Пугать отчаяньем готовым,
Приятной лестью забавлять,
Ловить минуту умиленья,
Невинных лет предубежденья
Умом и страстью побеждать,
Невольной ласки ожидать,
Молить и требовать признанья,
Подслушать сердца первый звук,
Преследовать любовь, и вдруг
Добиться тайного свиданья...
И после ей наедине
Давать уроки в тишине!
XII
Как рано мог уж он тревожить
Сердца кокеток записных!
Когда ж хотелось уничтожить
Ему соперников своих,
Как он язвительно злословил!
Какие сети им готовил!
Но вы, блаженные мужья,
С ним оставались вы друзья:
Его ласкал супруг лукавый,
Фобласа давний ученик,
И недоверчивый старик,
И рогоносец величавый,
Всегда довольный сам собой,
Своим обедом и женой.
XIII. XIV

XV
Бывало, он еще в постеле:
К нему записочки несут.
Что? Приглашенья? В самом деле,
Три дома на вечер зовут:
Там будет бал, там детский праздник.
Куда ж поскачет мой проказник?
С кого начнет он? Все равно:
Везде поспеть немудрено.
Покамест в утреннем уборе,
Надев широкий боливар 3,
Онегин едет на бульвар
И там гуляет на просторе,
Пока недремлющий брегет
Не прозвонит ему обед.
XVI
Уж тёмно: в санки он садится.
«Пади, пади!» — раздался крик;
Морозной пылью серебрится
Его бобровый воротник.
К Talon 4 помчался: он уверен,
Что там уж ждет его Каверин.
Вошел: и пробка в потолок,
Вина кометы брызнул ток;
Пред ним roast-beef окровавленный,
И трюфли, роскошь юных лет,
Французской кухни лучший цвет,
И Страсбурга пирог нетленный
Меж сыром лимбургским живым
И ананасом золотым.
XVII
Еще бокалов жажда просит
Залить горячий жир котлет,
Но звон брегета им доносит,
Что новый начался балет.
Театра злой законодатель,
Непостоянный обожатель
Очаровательных актрис,
Почетный гражданин кулис,
Онегин полетел к театру,
Где каждый, вольностью дыша,
Готов охлопать entrechat,
Обшикать Федру, Клеопатру,
Моину вызвать (для того,
Чтоб только слышали его).
XVIII
Волшебный край! там в стары годы,
Сатиры смелый властелин,
Блистал Фонвизин, друг свободы,
И переимчивый Княжнин;
Там Озеров невольны дани
Народных слез, рукоплесканий
С младой Семеновой делил;
Там наш Катенин воскресил
Корнеля гений величавый;
Там вывел колкий Шаховской
Своих комедий шумный рой,
Там и Дидло венчался славой,
Там, там под сению кулис
Младые дни мои неслись.
XIX
Мои богини! что вы? где вы?
Внемлите мой печальный глас:
Всё те же ль вы? другие ль девы,
Сменив, не заменили вас?
Услышу ль вновь я ваши хоры?
Узрю ли русской Терпсихоры
Душой исполненный полет?
Иль взор унылый не найдет
Знакомых лиц на сцене скучной,
И, устремив на чуждый свет
Разочарованный лорнет,
Веселья зритель равнодушный,
Безмолвно буду я зевать
И о былом воспоминать?
XX
Театр уж полон; ложи блещут;
Партер и кресла — все кипит;
В райке нетерпеливо плещут,
И, взвившись, занавес шумит.
Блистательна, полувоздушна,
Смычку волшебному послушна,
Толпою нимф окружена,
Стоит Истомина; она,
Одной ногой касаясь пола,
Другою медленно кружит,
И вдруг прыжок, и вдруг летит,
Летит, как пух от уст Эола;
То стан совьет, то разовьет
И быстрой ножкой ножку бьет.
XXI
Все хлопает. Онегин входит,
Идет меж кресел по ногам,
Двойной лорнет скосясь наводит
На ложи незнакомых дам;
Все ярусы окинул взором,
Всё видел: лицами, убором
Ужасно недоволен он;
С мужчинами со всех сторон
Раскланялся, потом на сцену
В большом рассеянье взглянул,
Отворотился — и зевнул,
И молвил: «Всех пора на смену;
Балеты долго я терпел,
Но и Дидло мне надоел» 5.
XXII
Еще амуры, черти, змеи
На сцене скачут и шумят;
Еще усталые лакеи
На шубах у подъезда спят;
Еще не перестали топать,
Сморкаться, кашлять, шикать, хлопать;
Еще снаружи и внутри
Везде блистают фонари;
Еще, прозябнув, бьются кони,
Наскуча упряжью своей,
И кучера, вокруг огней,
Бранят господ и бьют в ладони —
А уж Онегин вышел вон;
Домой одеться едет он.
XXIII
Изображу ль в картине верной
Уединенный кабинет,
Где мод воспитанник примерный
Одет, раздет и вновь одет?
Все, чем для прихоти обильной
Торгует Лондон щепетильный
И по Балтическим волнам
За лес и сало возит нам,
Все, что в Париже вкус голодный,
Полезный промысел избрав,
Изобретает для забав,
Для роскоши, для неги модной, —
Все украшало кабинет
Философа в осьмнадцать лет.
XXIV
Янтарь на трубках Цареграда,
Фарфор и бронза на столе,
И, чувств изнеженных отрада,
Духи в граненом хрустале;
Гребенки, пилочки стальные,
Прямые ножницы, кривые
И щетки тридцати родов
И для ногтей и для зубов.
Руссо (замечу мимоходом)
Не мог понять, как важный Грим
Смел чистить ногти перед ним,
Красноречивым сумасбродом 6.
Защитник вольности и прав
В сем случае совсем неправ.
XXV
Быть можно дельным человеком
И думать о красе ногтей:
К чему бесплодно спорить с веком?
Обычай деспот меж людей.
Второй Чадаев, мой Евгений,
Боясь ревнивых осуждений,
В своей одежде был педант
И то, что мы назвали франт.
Он три часа по крайней мере
Пред зеркалами проводил
И из уборной выходил
Подобный ветреной Венере,
Когда, надев мужской наряд,
Богиня едет в маскарад.
XXVI
В последнем вкусе туалетом
Заняв ваш любопытный взгляд,
Я мог бы пред ученым светом
Здесь описать его наряд;
Конечно б это было смело,
Описывать мое же дело:
Но панталоны, фрак, жилет,
Всех этих слов на русском нет;
А вижу я, винюсь пред вами,
Что уж и так мой бедный слог
Пестреть гораздо б меньше мог
Иноплеменными словами,
Хоть и заглядывал я встарь
В Академический словарь.
XXVII
У нас теперь не то в предмете:
Мы лучше поспешим на бал,
Куда стремглав в ямской карете
Уж мой Онегин поскакал.
Перед померкшими домами
Вдоль сонной улицы рядами
Двойные фонари карет
Веселый изливают свет
И радуги на снег наводят;
Усеян плошками кругом,
Блестит великолепный дом;
По цельным окнам тени ходят,
Мелькают профили голов
И дам и модных чудаков.
XXVIII
Вот наш герой подъехал к сеням;
Швейцара мимо он стрелой
Взлетел по мраморным ступеням,
Расправил волоса рукой,
Вошел. Полна народу зала;
Музыка уж греметь устала;
Толпа мазуркой занята;
Кругом и шум и теснота;
Бренчат кавалергарда шпоры;
Летают ножки милых дам;
По их пленительным следам
Летают пламенные взоры,
И ревом скрыпок заглушен
Ревнивый шепот модных жен.
XXIX
Во дни веселий и желаний
Я был от балов без ума:
Верней нет места для признаний
И для вручения письма.
О вы, почтенные супруги!
Вам предложу свои услуги;
Прошу мою заметить речь:
Я вас хочу предостеречь.
Вы также, маменьки, построже
За дочерьми смотрите вслед:
Держите прямо свой лорнет!
Не то... не то, избави боже!
Я это потому пишу,
Что уж давно я не грешу.
XXX
Увы, на разные забавы
Я много жизни погубил!
Но если б не страдали нравы,
Я балы б до сих пор любил.
Люблю я бешеную младость,
И тесноту, и блеск, и радость,
И дам обдуманный наряд;
Люблю их ножки; только вряд
Найдете вы в России целой
Три пары стройных женских ног.
Ах! долго я забыть не мог
Две ножки... Грустный, охладелый,
Я всё их помню, и во сне
Они тревожат сердце мне.
XXXI
Когда ж и где, в какой пустыне,
Безумец, их забудешь ты?
Ах, ножки, ножки! где вы ныне?
Где мнете вешние цветы?
Взлелеяны в восточной неге,
На северном, печальном снеге
Вы не оставили следов:
Любили мягких вы ковров
Роскошное прикосновенье.
Давно ль для вас я забывал
И жажду славы и похвал,
И край отцов, и заточенье?
Исчезло счастье юных лет,
Как на лугах ваш легкий след.
XXXII
Дианы грудь, ланиты Флоры
Прелестны, милые друзья!
Однако ножка Терпсихоры
Прелестней чем-то для меня.
Она, пророчествуя взгляду
Неоцененную награду,
Влечет условною красой
Желаний своевольный рой.
Люблю ее, мой друг Эльвина,
Под длинной скатертью столов,
Весной на мураве лугов,
Зимой на чугуне камина,
На зеркальном паркете зал,
У моря на граните скал.
XXXIII
Я помню море пред грозою:
Как я завидовал волнам,
Бегущим бурной чередою
С любовью лечь к ее ногам!
Как я желал тогда с волнами
Коснуться милых ног устами!
Нет, никогда средь пылких дней
Кипящей младости моей
Я не желал с таким мученьем
Лобзать уста младых Армид,
Иль розы пламенных ланит,
Иль перси, полные томленьем;
Нет, никогда порыв страстей
Так не терзал души моей!
XXXIV
Мне памятно другое время!
В заветных иногда мечтах
Держу я счастливое стремя...
И ножку чувствую в руках;
Опять кипит воображенье,
Опять ее прикосновенье
Зажгло в увядшем сердце кровь,
Опять тоска, опять любовь!..
Но полно прославлять надменных
Болтливой лирою своей;
Они не стоят ни страстей,
Ни песен, ими вдохновенных:
Слова и взор волшебниц сих
Обманчивы... как ножки их.
XXXV
Что ж мой Онегин? Полусонный
В постелю с бала едет он:
А Петербург неугомонный
Уж барабаном пробужден.
Встает купец, идет разносчик,
На биржу тянется извозчик,
С кувшином охтенка спешит,
Под ней снег утренний хрустит.
Проснулся утра шум приятный.
Открыты ставни; трубный дым
Столбом восходит голубым,
И хлебник, немец аккуратный,
В бумажном колпаке, не раз
Уж отворял свой васисдас.
XXXVI
Но, шумом бала утомленный
И утро в полночь обратя,
Спокойно спит в тени блаженной
Забав и роскоши дитя.
Проснется за полдень, и снова
До утра жизнь его готова,
Однообразна и пестра.
И завтра то же, что вчера.
Но был ли счастлив мой Евгений,
Свободный, в цвете лучших лет,
Среди блистательных побед,
Среди вседневных наслаждений?
Вотще ли был он средь пиров
Неосторожен и здоров?
XXXVII
Нет: рано чувства в нем остыли;
Ему наскучил света шум;
Красавицы не долго были
Предмет его привычных дум;
Измены утомить успели;
Друзья и дружба надоели,
Затем, что не всегда же мог
Beef-steaks и страсбургский пирог
Шампанской обливать бутылкой
И сыпать острые слова,
Когда болела голова;
И хоть он был повеса пылкой,
Но разлюбил он наконец
И брань, и саблю, и свинец.
XXXVIII
Недуг, которого причину
Давно бы отыскать пора,
Подобный английскому сплину,
Короче: русская хандра
Им овладела понемногу;
Он застрелиться, слава богу,
Попробовать не захотел,
Но к жизни вовсе охладел.
Как Child-Harold, угрюмый, томный
В гостиных появлялся он;
Ни сплетни света, ни бостон,
Ни милый взгляд, ни вздох нескромный,
Ничто не трогало его,
Не замечал он ничего.
XXXIX. XL. XLI

XLII
Причудницы большого света!
Всех прежде вас оставил он;
И правда то, что в наши лета
Довольно скучен высший тон;
Хоть, может быть, иная дама
Толкует Сея и Бентама,
Но вообще их разговор
Несносный, хоть невинный вздор;
К тому ж они так непорочны,
Так величавы, так умны,
Так благочестия полны,
Так осмотрительны, так точны,
Так неприступны для мужчин,
Что вид их уж рождает сплин 7.
XLIII
И вы, красотки молодые,
Которых позднею порой
Уносят дрожки удалые
По петербургской мостовой,
И вас покинул мой Евгений.
Отступник бурных наслаждений,
Онегин дома заперся,
Зевая, за перо взялся,
Хотел писать — но труд упорный
Ему был тошен; ничего
Не вышло из пера его,
И не попал он в цех задорный
Людей, о коих не сужу,
Затем, что к ним принадлежу.
XLIV
И снова, преданный безделью,
Томясь душевной пустотой,
Уселся он — с похвальной целью
Себе присвоить ум чужой;
Отрядом книг уставил полку,
Читал, читал, а всё без толку:
Там скука, там обман иль бред;
В том совести, в том смысла нет;
На всех различные вериги;
И устарела старина,
И старым бредит новизна.
Как женщин, он оставил книги,
И полку, с пыльной их семьей,
Задернул траурной тафтой.
XLV
Условий света свергнув бремя,
Как он, отстав от суеты,
С ним подружился я в то время.
Мне нравились его черты,
Мечтам невольная преданность,
Неподражательная странность
И резкий, охлажденный ум.
Я был озлоблен, он угрюм;
Страстей игру мы знали оба;
Томила жизнь обоих нас;
В обоих сердца жар угас;
Обоих ожидала злоба
Слепой Фортуны и людей
На самом утре наших дней.
XLVI
Кто жил и мыслил, тот не может
В душе не презирать людей;
Кто чувствовал, того тревожит
Призрак невозвратимых дней:
Тому уж нет очарований,
Того змия воспоминаний,
Того раскаянье грызет.
Все это часто придает
Большую прелесть разговору.
Сперва Онегина язык
Меня смущал; но я привык
К его язвительному спору,
И к шутке, с желчью пополам,
И злости мрачных эпиграмм.
XLVII
Как часто летнею порою,
Когда прозрачно и светло
Ночное небо над Невою 8
И вод веселое стекло
Не отражает лик Дианы,
Воспомня прежних лет романы,
Воспомня прежнюю любовь,
Чувствительны, беспечны вновь,
Дыханьем ночи благосклонной
Безмолвно упивались мы!
Как в лес зеленый из тюрьмы
Перенесен колодник сонный,
Так уносились мы мечтой
К началу жизни молодой.
XLVIII
С душою, полной сожалений,
И опершися на гранит,
Стоял задумчиво Евгений,
Как описал себя пиит 9.
Все было тихо; лишь ночные
Перекликались часовые,
Да дрожек отдаленный стук
С Мильонной раздавался вдруг;
Лишь лодка, веслами махая,
Плыла по дремлющей реке:
И нас пленяли вдалеке
Рожок и песня удалая...
Но слаще, средь ночных забав,
Напев Торкватовых октав!
XLIX
Адриатические волны,
О Брента! нет, увижу вас
И, вдохновенья снова полный,
Услышу ваш волшебный глас!
Он свят для внуков Аполлона;
По гордой лире Альбиона
Он мне знаком, он мне родной.
Ночей Италии златой
Я негой наслажусь на воле,
С венецианкою младой,
То говорливой, то немой,
Плывя в таинственной гондоле;
С ней обретут уста мои
Язык Петрарки и любви.
L
Придет ли час моей свободы?
Пора, пора! — взываю к ней;
Брожу над морем 10, жду погоды,
Маню ветрила кораблей.
Под ризой бурь, с волнами споря,
По вольному распутью моря
Когда ж начну я вольный бег?
Пора покинуть скучный брег
Мне неприязненной стихии
И средь полуденных зыбей,
Под небом Африки моей 11,
Вздыхать о сумрачной России,
Где я страдал, где я любил,
Где сердце я похоронил.
LI
Онегин был готов со мною
Увидеть чуждые страны;
Но скоро были мы судьбою
На долгой срок разведены.
Отец его тогда скончался.
Перед Онегиным собрался
Заимодавцев жадный полк.
У каждого свой ум и толк:
Евгений, тяжбы ненавидя,
Довольный жребием своим,
Наследство предоставил им,
Большой потери в том не видя
Иль предузнав издалека
Кончину дяди старика.
LII
Вдруг получил он в самом деле
От управителя доклад,
Что дядя при смерти в постеле
И с ним проститься был бы рад.
Прочтя печальное посланье,
Евгений тотчас на свиданье
Стремглав по почте поскакал
И уж заранее зевал,
Приготовляясь, денег ради,
На вздохи, скуку и обман
(И тем я начал мой роман);
Но, прилетев в деревню дяди,
Его нашел уж на столе,
Как дань готовую земле.
LIII
Нашел он полон двор услуги;
К покойнику со всех сторон
Съезжались недруги и други,
Охотники до похорон.
Покойника похоронили.
Попы и гости ели, пили
И после важно разошлись,
Как будто делом занялись.
Вот наш Онегин — сельский житель,
Заводов, вод, лесов, земель
Хозяин полный, а досель
Порядка враг и расточитель,
И очень рад, что прежний путь
Переменил на что-нибудь.
LIV
Два дня ему казались новы
Уединенные поля,
Прохлада сумрачной дубровы,
Журчанье тихого ручья;
На третий роща, холм и поле
Его не занимали боле;
Потом уж наводили сон;
Потом увидел ясно он,
Что и в деревне скука та же,
Хоть нет ни улиц, ни дворцов,
Ни карт, ни балов, ни стихов.
Хандра ждала его на страже,
И бегала за ним она,
Как тень иль верная жена.
LV
Я был рожден для жизни мирной,
Для деревенской тишины;
В глуши звучнее голос лирный,
Живее творческие сны.
Досугам посвятясь невинным,
Брожу над озером пустынным,
И far niente мой закон.
Я каждым утром пробужден
Для сладкой неги и свободы:
Читаю мало, долго сплю,
Летучей славы не ловлю.
Не так ли я в былые годы
Провел в бездействии, в тени
Мои счастливейшие дни?
LVI
Цветы, любовь, деревня, праздность,
Поля! я предан вам душой.
Всегда я рад заметить разность
Между Онегиным и мной,
Чтобы насмешливый читатель
Или какой-нибудь издатель
Замысловатой клеветы,
Сличая здесь мои черты,
Не повторял потом безбожно,
Что намарал я свой портрет,
Как Байрон, гордости поэт,
Как будто нам уж невозможно
Писать поэмы о другом,
Как только о себе самом.
LVII
Замечу кстати: все поэты —
Любви мечтательной друзья.
Бывало, милые предметы
Мне снились, и душа моя
Их образ тайный сохранила;
Их после муза оживила:
Так я, беспечен, воспевал
И деву гор, мой идеал,
И пленниц берегов Салгира.
Теперь от вас, мои друзья,
Вопрос нередко слышу я:
«О ком твоя вздыхает лира?
Кому, в толпе ревнивых дев,
Ты посвятил ее напев?
LVIII
Чей взор, волнуя вдохновенье,
Умильной лаской наградил
Твое задумчивое пенье?
Кого твой стих боготворил?»
И, други, никого, ей-богу!
Любви безумную тревогу
Я безотрадно испытал.
Блажен, кто с нею сочетал
Горячку рифм: он тем удвоил
Поэзии священный бред,
Петрарке шествуя вослед,
А муки сердца успокоил,
Поймал и славу между тем;
Но я, любя, был глуп и нем.
LIX
Прошла любовь, явилась муза,
И прояснился темный ум.
Свободен, вновь ищу союза
Волшебных звуков, чувств и дум;
Пишу, и сердце не тоскует,
Перо, забывшись, не рисует,
Близ неоконченных стихов,
Ни женских ножек, ни голов;
Погасший пепел уж не вспыхнет,
Я всё грущу; но слез уж нет,
И скоро, скоро бури след
В душе моей совсем утихнет:
Тогда-то я начну писать
Поэму песен в двадцать пять.
LX
Я думал уж о форме плана
И как героя назову;
Покамест моего романа
Я кончил первую главу;
Пересмотрел все это строго:
Противоречий очень много,
Но их исправить не хочу.
Цензуре долг свой заплачу
И журналистам на съеденье
Плоды трудов моих отдам:
Иди же к невским берегам,
Новорожденное творенье,
И заслужи мне славы дань:
Кривые толки, шум и брань!
    """.replace("\n", "<br>\n")
    return text


@app.route('/index')
def index():
    images = {
        "cat1": {
            "text": "кот",
            "url": "https://thiscatdoesnotexist.com/"
        },
        "cat2": {
            "text": "рисунок",
            "url": "https://thisartworkdoesnotexist.com/"
        },
        "cat3": {
            "text": "лошадь",
            "url": "https://thishorsedoesnotexist.com/"
        },
        "c4": {
            "c2": "text"
        }
    }
    names = [
        "привет",
        "это самый лучший сайт",
        "как дела?",
        "не придумал("
    ]
    number = random.randint(0, 3)

    return render_template(
        "index.html",
        images=images,
        num=number,
    )


@app.route('/user/<name>')
def show_user_profile1(name):
    text = f"Привет, {name}"
    return text


@app.route('/read/<int:page>')
def read(page):
    url = f'https://ilibrary.ru/text/436/p.{str(page)}/index.html'
    page = requests.get(url)
    # Проверим подключение:
    print(page.status_code)

    new_news = []
    news = []

    soup = BeautifulSoup(page.text, "html.parser")

    news = soup.findAll('span', class_='pmm')

    for i in range(len(news)):
        news[i] = str(news[i])
    print(news)
    print(type(page))
    return f"""
<html>
<title>Евгений Онегин</title>
<body>
{news[0]}
<p>
    <a href=f'https://ilibrary.ru/text/436/p.{int(str(page)) - 1}/index.html'>предыдущая страница</a>
    <a href=f'https://ilibrary.ru/text/436/p.{int(str(page)) + 1}/index.html'>следующая страница</a>
</p>
</body>
</html>
"""


app.run(debug=True)
