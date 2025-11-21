import pandas as pd

from reports import get_report
from utils.csv_io import read_rows_from_files


def test_performance_report():
    data_for_file1 = [
        ('name', 'position', 'completed_tasks', 'performance', 'skills', 'team', 'experience_years'),
        ('David Chen', 'Mobile Developer', '36', '4.6', 'Swift, Kotlin, React Native, iOS', 'Mobile Team', '3'),
        ('Elena Popova', 'Backend Developer', '43', '4.8', 'Java, Spring Boot, MySQL, Redis', 'API Team', '4'),
        ('Chris Wilson', 'DevOps Engineer', '39', '4.7', 'Docker, Jenkins, GitLab CI, AWS', 'Infrastructure Team', '5')
    ]
    data_for_file2 = [
        ('name', 'position', 'completed_tasks', 'performance', 'skills', 'team', 'experience_years'),
        ('Alex Ivanov', 'Backend Developer', '45', '4.8', 'Python, Django, PostgreSQL, Docker', 'API Team', '5'),
        ('Maria Petrova', 'Backend Developer', '38', '4.7', 'Python, Django, PostgreSQL, Docker', 'Web Team', '4'),
        ('John Smith', 'Mobile Developer', '29', '4.6', 'Swift, Kotlin, React Native, iOS', 'AI Team', '3')
    
    ]
    df1 = pd.DataFrame(data_for_file1[1:], columns=data_for_file1[0])
    df2 = pd.DataFrame(data_for_file2[1:], columns=data_for_file2[0])

    df1.to_csv('employees111.csv', index=False)
    df2.to_csv('employees222.csv', index=False)

    rows = read_rows_from_files([str('employees111.csv'), str('employees222.csv')])
    report = get_report('performance')
    headers, data = report.compute(rows)
    result = {pos: val for pos, val in data}
    # Backend Developer: (4.8 + 4.8 + 4.7) / 3 = 4.76
    # Mobile Developer: (4.6 + 4.6) / 2 = 4.6
    assert result['Backend Developer'] == 4.77
    assert result['Mobile Developer'] == 4.6