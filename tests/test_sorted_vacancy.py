import pytest
from src.hh_connection import GetHeadHunter
from src.sorted_vacancies import SortedVacancy


@pytest.fixture
def test_head_hunter():
    return GetHeadHunter("python", 1)


def test_sorted_vacancy():
    """
    Проверка на наличие 2-ух экземпляров класса
    """
    r = SortedVacancy()
    assert r.head_hunter_sorted == []
    assert r.date_format is None


def test_sorted_vacancies_hh():
    """
     Проверка на работоспособность сортировки вакансии
    """
    r = SortedVacancy()
    assert r.sorted_vacancies_hh == [{'city': 'Санкт-Петербург',
                                      'date': '26.01.2024',
                                      'name': 'Middle Python Developer',
                                      'payment_1': 100000,
                                      'payment_2': 120000,
                                      'skill_1': 'От 2-х лет коммерческого опыта, знаешь что такое SOLID, DRY, '
                                                 'KISS, интересуешься паттернами проектирования. Знаешь '
                                                 '<highlighttext>Python</highlighttext> 3.8. ',
                                      'skill_2': 'Участвовать во всех этапах разработки в составе scrum-команды: '
                                                 'собирать и анализировать требования, декомпозировать и оценивать '
                                                 'задачи, писать код, релизить...'}]


def test_error_vacancies_sorted():
    """
    Проверка на наличие ошибок
    """
    with pytest.raises(TypeError):
        SortedVacancy(100)
