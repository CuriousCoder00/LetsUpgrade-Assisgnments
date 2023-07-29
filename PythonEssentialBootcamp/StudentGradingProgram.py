def calGrade(marks):
    if marks >= 90:
        return 'A+'
    elif 80 <= marks < 90:
        return 'A'
    elif 70 <= marks < 80:
        return 'B'
    elif 60 <= marks < 70:
        return 'C'
    elif 50 <= marks < 60:
        return 'D'
    else:
        return 'Fail'

def getValMarks():
    while True:
        try:
            marks = int(input('Enter the marks obtained by the student: '))
            if marks >= 0 and marks <= 100:
                return marks
            else:
                print('Marks should be between 0 and 100. Please try agian.')
        except ValueError:
            print('Invalid Input. Please enter a valid value for marks.')


def main():
    print('Student Grading Program')
    while True:
        marks = getValMarks()
        grade = calGrade(marks)
        print(f'Grade: {grade}')

        choice = input("Do you want to calculate grade for another student? (yes/no):").lower()
        if choice == 'no':
            break

if __name__ == "__main__":
    main()