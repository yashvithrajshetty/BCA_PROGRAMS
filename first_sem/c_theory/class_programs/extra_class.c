// c pgm to perform arithmatic operation of two integers
#include<stdio.h>  //header file defined to perform input and output operation
int main(){
    int firstnumber,sum,difference;  //declared a variable 'firstnumber' of 'integer' type.
    int secoundnumber;
    firstnumber=100;  //value 100 is stored in 'firstnumber'
    secoundnumber=200;  // value initialization
    sum=firstnumber + secoundnumber;  //addition
    printf("the sum is:%d",sum);

    float first,secound;
    printf("enter the first number");  //read a float type data from KB and stores it in 'first'
    scanf("%f",&first);

    printf("enter the secound number");  //read a float type data from KB and stores it in 'secound'
    scanf("%f",&secound);

    difference=first - secound;
    printf("the difference is %f",difference);
    