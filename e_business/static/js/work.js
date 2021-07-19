var updateBtns= document.getElementsByClassName('update-cart')

for (var i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){

        var Productid= this.dataset.product
        var action= this.dataset.action
        console.log('Productid:', Productid, 'action:', action)
        console.log('USER:', user)
        console.log(this.dataset.product)
        if (user==='AnonymousUser'){
            /* addCookieItem(Productid, action) */
            window.location.assign("/login")
            alert("Please sign in to proceed...") 
        }else{
           
            UserOrderUpdate(Productid, action)
        }

    })

} 


function addCookieItem(Productid, action){

    console.log("User not logged in")

    if(action == 'add'){
        if(cart[Productid] == undefined){
            cart[Productid] = {'quantity':1}
        }else{
            cart[Productid]['quantity'] += 1
        }
    }

    if(action == 'remove'){
        cart[Productid]['quantity'] -= 1

        if(cart[Productid]['quantity']<= 0){
            console.log('Remove Item')
            delete cart[Productid]
        }
    }
    //console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path/"
    location.reload()

}


function UserOrderUpdate(Productid, action){
    console.log("User is logged in, data sending...")
    var url = 'update_item'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'Productid':Productid, 'action':action })
    })
    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data:', data)
        location.reload()
    })
       
}