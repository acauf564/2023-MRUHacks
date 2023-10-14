import PDFtoLIST
from deliverable import Assignment



def main():
    pdf_to_list = PDFtoLIST.PDFtoList()
    assignmentsTextList = pdf_to_list.getResponse()
    assignmentsObjectList = parseToObjects(assignmentsTextList)
    
    # for i in assignmentsObjectList:
    #     print(i)

    table = get_table(assignmentsObjectList)
    return table

def parseToObjects(list):
    course = []
    for i in list:
        newAssignment = Assignment(i[0], i[1], i[2])
        # print(str(newAssignment.getDescription()))
        course.append(newAssignment)
    return course

def get_table(assignmentsObjectList):
    html_table = "<table>"
    html_table += "<tr><th>Description</th> <th>Date</th> <th>Weight</th> <th>Est. Time</th></tr>"
    for row in assignmentsObjectList:
        html_table +="<tr>"
        for item in row.getTableList():
            html_table += f"<td>{item}</td>"
    html_table += "</tr>"
    html_table += "</table>"
    
    return html_table

def display_table(table):
    with open("/templates/table.html", "w") as f:
        f.write(table)

    f.close()

main()