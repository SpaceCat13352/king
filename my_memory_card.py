from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle, randint
 
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # все строки надо задать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
questions_list = [] 
questions_list.append(Question('я сам задам вопрос а вы отгодайте', 'Правильно', 'Неправильно', 'Неправильно', 'Неправильно'))
questions_list.append(Question('В каком случае, смотря на цифру 2, человек произносит «десять»?', 'Когда на электронных часах 22:00', 'Когда на электронных часах 10:00', 'Когда на электронных часах 12:00', 'Когда на электронных часах 20:00'))
questions_list.append(Question('Человек при жизни получает это трижды: два раза абсолютно бесплатно, на третий раз ему приходится за это платить, о чем идет речь', 'о зубах', 'о купонах', 'о пробных занятиях', 'о еде'))
questions_list.append(Question('Вите и Сереже купили по коробке конфет. В каждой коробке лежит 12 конфет. Витя из своей коробки съел несколько штук, а Сережа из своей съел столько, сколько осталось в коробке у Вити, сколько конфет осталось на двоих у Вити и Сережи', '12', '8', '9', '10'))
questions_list.append(Question('Паша засунул в бутылку монетку и заткнул бутылку пробкой. Затем он достал монетку, не вынимая пробки и не разбивая бутылки', 'Он протолкнул пробку внутрь бутылки', 'Он открыл бутылку и достал монету', 'Он разбил бутылку и достал монету', 'Он подождал пока бутылка не распадётся на атомы и заберёт монету'))
questions_list.append(Question('Каких камней не бывает в речке?', 'сухих', 'драгоценных', 'морских', 'красивых'))
questions_list.append(Question('На столе лежат две монеты, в сумме они дают 3 рубля. Одна из них — не 1 рубль. Какие это монеты?', 'На столе лежат 2 рубля и 1 рубль', 'На столе лежат 1 рубля и 2 рубль', 'На столе лежат 1 рубля и 1 рубль и ещё 1 рубль', 'На столе лежат 3 рубля'))
questions_list.append(Question('Что не вместится даже в самую большую кастрюлю?', 'доброта нашей учительницы', 'самый большой камень', 'крышка от кастрюли', 'океан'))
questions_list.append(Question('Что может в одно и то же время стоять и ходить, висеть и стоять, ходить и лежать?', 'часы', 'моё терпение', 'камень', 'курсор мыши'))
questions_list.append(Question('Завязать можно, а развязать нельзя. Что это такое?', 'разговор', 'шнурки от наушников', 'шнурки от красовок', 'узел корторый ты сам придумал'))

app = QApplication([])
 
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса
 
RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
 
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # скроем панель с ответом, сначала должна быть видна панель вопросов
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    # сбросить выбранную радио-кнопку
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ 
    show_question() # показываем панель вопросов 
 
def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
        window. score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ',window.score)
        print('Рейтинг: ', (window.score/window.total*100))
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')

            
 
def next_question():
    ''' задает следующий вопрос из списка '''
    # этой функции нужна переменная, в которой будет указываться номер текущего вопроса
    # эту переменную можно сделать глобальной, либо же сделать свойством "глобального объекта" (app или window)
    # мы заведем (ниже) свойство window.cur_question.
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q) # спросили
 
def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос
 
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
# текущий вопрос из списка сделаем свойством объекта "окно", так мы сможем спокойно менять его из функции:
window.cur_question = -1    # по-хорошему такие переменные должны быть свойствами, 
                            # только надо писать класс, экземпляры которого получат такие свойства, 
                            # но python позволяет создать свойство у отдельно взятого экземпляра
 
btn_OK.clicked.connect(click_OK) # по нажатии на кнопку выбираем, что конкретно происходит
 
# все настроено, осталось задать вопрос и показать окно:
window.score = 0
window.total = 0
next_question()
window.resize(1500, 900)
window.show()
app.exec()
