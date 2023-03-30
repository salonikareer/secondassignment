element={"apple","orange","banana","pineapple","guava"}

#ACCESS ONE ELEMENT FROM SET 
#In keyword species that the element is present in the set or not
print("banana" in element);
print("peach" in element);






tup1=("apple","banana","orange","guava");
#append by converting to list
x=list(tup1);
x.append("sakshi");
tup1=tuple(x);
print(tup1);

#add tuple to tuple
tup2=("pineapple",);
tup1+=tup2;
print(tup1);



mydict={
    "student":"sakshi",
    "id":585,
    "designation":"student"
}
#BY USING copy() this does not take any parameter
dict1=mydict.copy();
print(dict1);

#BY USING dict() it takes dictionary as a parameter
dict2=dict(mydict);
print(dict2);



lement={"apple","orange","banana","pineapple","guava"};
element1={"bus","car","train","orange","guava"};

#BY USING intersection_update()
#this method will keep only the items that present in both the sets
element.intersection_update(element1)
print(element);


element={"apple","orange","banana","pineapple","guava"};

#bY USING remove()
#if ur removing item is not present in the set then remove give us a error
element.remove("guava");
print(element);

#we use repeat use remove item as guava then they give us error
#element.remove("guava");
#print(element);

#BY USING discard()
#if ur removing item is not present in the set then discard doesn't give us a error
element.discard("banana");
print(element);

#we use repeat use remove item as banana then they doesn't give us error
element.discard("banana");
print(element);



element={"apple","orange","banana","pineapple","guava"};
element1={"bus","car","train","orange","guava"};
#BY USING symmetric_differnce()
#this method will return a new set that contains only the items that are not present in both the sets
z = element.symmetric_difference(element1);
print(z);








element={"apple","orange","banana","pineapple","guava"};
element1={"bus","car","train","orange","guava"};

#BY USING symmetric_difference_update()
#this method will keep only the items that not present in both the sets
element.symmetric_difference_update(element1);
print(element);