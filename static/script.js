
console.log('Hello world')
const one =document.getElementById('first')
const tow =document.getElementById('second')
const three =document.getElementById('third')
const four =document.getElementById('fourth')
const five =document.getElementById('fifth')

const form =document.querySelector('.rate-form')
const confirmBox=document.getElementById('confirm-box')

const csrf=document.getElementsByName('csrfmiddlewaretoken')

console.log(form)
console.log(confirmBox)
console.log(csrf)

const handelStarSelect=(size)=>{
    const children=form.children
  for(let i=0;i<children.length;i++){
    if(i<=size){
        children[i].classList.add('checked')
    
    }
    else{
        children[i].classList.remove('checked')
    

    }
  }

}
const handelSelect=(selection)=>{
    switch(selection){
        case 'first':{
            // one.classList.add('checked')
            // tow.classList.remove('checked')
            // three.classList.remove('checked')
            // four.classList.remove('checked')
            // five.classList.remove('checked')
            handelStarSelect(1)
            return
            
        }
        case 'second':{
            handelStarSelect(2)
            return
            
        }
        case 'third':{
           handelStarSelect(3)
            return
            
        }
        case 'fourth':{
            handelStarSelect(4)
            return
            
        }
        case 'fifth':{
            handelStarSelect(5)
            return
            
        }
    }

}
const getNumericValue=(stringVlaue)=>{
    let numericVlaue;
    if(stringVlaue==='first'){
        numericVlaue=1

    }
    else if(stringVlaue==='second'){
        numericVlaue=2
    }
    else if(stringVlaue==='third'){
        numericVlaue=3
    }
    
    else if(stringVlaue==='fourth'){
        numericVlaue=4
    }
    else if(stringVlaue==='fifth'){
        numericVlaue=5
    }
    else{
        numericVlaue=0
    }
    return numericVlaue
}



if(one){
    const arr=[one,tow,three,four,five]

arr.forEach(item=>item.addEventListener('mouseover',(event)=>{
    handelSelect(event.target.id)
   
}))
arr.forEach(item=>item.addEventListener('click',(event)=>{
   const val=event.target.id
   console.log("val :",val);


   let isSubmit = false
   form.addEventListener('submit',e=>{
    e.preventDefault()
    if(isSubmit){
        return
    }
    isSubmit=true
    //recipe id
    const id=e.target.id
    console.log("id :",id)
    //value of the rating translated into numeric
    const val_num=getNumericValue(val)
    console.log(val_num);
 
    $.ajax({
        type:'POST',
        url:`/${id}/rating/`,
        data:{
            'csrfmiddlewaretoken':csrf[0].value,
            'id':id,
            'val':val_num
        },
       
    
        })
    

    
   })


})

)}




