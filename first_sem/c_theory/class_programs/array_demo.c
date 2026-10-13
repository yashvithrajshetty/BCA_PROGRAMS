//pgm to store and display 5 subject marks
//for student
#include<stdio.h>
int main(){
    int my_marks[5];
    int sub_marks[5];
    //with SIZE 5 of 'int' type
    //storing data/ ARRAY inisitialization - array_name[index]=data/value;
    sub_marks[0]=80;
    sub_marks[1]=78;
    sub_marks[2]=68;
    sub_marks[3]=58;
    sub_marks[4]=88;   //static array initialization
    // fetch first array element from 'sub_marks'
    printf("First subject mark: %d",sub_marks[0]);
    //dynamic initialization of 'my_marks'
}

     for(int i=0;i<5;i++){
        printf("Enter %d subject marks:[int data]",i+1);
        scanf("%d",&my_marks[i]);  //stored in 1st location
}