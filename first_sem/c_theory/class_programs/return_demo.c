#include<stdio.h>
int rollno,sub1,sub2,sub3,sub4,sub5,total;
float avg,cgpa;          //global declaration
void getStudentData(){
    printf("enter rollnumber");
    scanf("%d",&rollno);
    printf("enter the sub1 mark ");
    scanf("%d",&sub1);
    printf("enter the sub2 mark ");
    scanf("%d",&sub2);
    printf("enter the sub3 mark ");
    scanf("%d",&sub3);
    printf("enter the sub4 mark ");
    scanf("%d",&sub4);
    printf("enter the sub5 mark ");
    scanf("%d",&sub5);
}

void gettotal(){
total=sub1+sub2+sub3+sub4+sub5;

}
void getaverage(){
avg=(sub1+sub2+sub3+sub4+sub5)/5;
}
void getCGPA(){

    
}

int main(){
    //declaration

    getStudentData();   //collect student data
    getTotal();         //calculate total of 5 subject marks
    getAverage();       //calculate average mark
    getCGPA();          //to get CGPA
    displayStudentDetails();      //to display student details

    print("the total is: %d",total);
}