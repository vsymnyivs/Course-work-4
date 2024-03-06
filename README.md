Проект, который получает информацию о вакансиях с платформы Head Hunter в России.
В данном проекте пользователь принимает активное участие, а именно: Пользователю необходимо ввести конкретные данные (необходимую вакансию, количество вакансий, заработную плату, город), чтобы получить конкретный результат. Программа запускается при помощи прямой ссылки "https://api.hh.ru/" по умолчанию. Так же есть возможность запуска при помощи API, для этого предусмотрин абстрактный класс, который работает с API

Что необходимо вводить: Вакансию (которая интересует пользователя. Если вакансию не указывать, программа упадет с предупреждением) Количество вакансий (то количество вакансий, которые хочет видеть пользователь. Максимум 100, если количество не указывается - программа падает с предупреждением) Минимальная заработная плата (происходит фильтрация заработной платы, если та меньше, то вакансия не учитывается. Если заработная плата не указывается, то выводятся все вакансии по умолчанию) Интересующий город (если город не указывается, то выводятся все города по умолчанию)

В данном проекте были применены приемы «абстрактных классов», «классов наследования», «тестирование» через pytest. Проект был сделан на виртуальном окружение «Venv». В проекте имеется файл «requirements.txt» со всеми зависимостями.