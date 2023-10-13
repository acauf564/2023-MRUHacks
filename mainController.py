import PDFtoLIST
from deliverable import Assignment


def main():
    pdf_to_list = PDFtoLIST.PDFtoList()
    assignmentsTextList = pdf_to_list.getResponse()
    assignmentsObjectList = parseToObjects(assignmentsTextList)
    print(assignmentsObjectList)


def parseToObjects(list):
    course = []
    for i in list:
        newAssignment = Assignment(i[0], i[1], i[2])
        course.append(newAssignment)
    return course


main()