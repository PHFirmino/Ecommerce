var attbotao = document.getElementsByClassName("att-cart")

for(var i = 0; i < attbotao.length; i++){
    attbotao[i].addEventListener("click", function(){
        var produtoId = this.dataset.produto
        var produtoAcao = this.dataset.acao 
        console.log('produtoID:',produtoId, 'produtoAcao:',produtoAcao)

        if(user === 'AnonymousUser'){
            addCookieItem(produtoId, produtoAcao)
        }else{
            attPedidoUser(produtoId, produtoAcao)
        }
    })
} 

function addCookieItem(produtoID, produtoAcao){
    console.log("O usuário não está logado")

    if(produtoAcao == 'add'){
        if(carrinho[produtoID] == undefined){
            carrinho[produtoID] = {'quantidade': 1}
        }else{
            carrinho[produtoID]['quantidade'] += 1
        }
    }

    if(produtoAcao == 'remover'){
        carrinho[produtoID]['quantidade'] -= 1
        if(carrinho[produtoID]['quantidade'] <= 0){
            console.log('Item removido')
            delete carrinho[produtoID]
        }
    }
    
    console.log('Carrinho: ', carrinho)
    document.cookie = 'carrinho=' + JSON.stringify(carrinho) + ";domain;path=/"
    location.reload()
}


function attPedidoUser(produtoID, produtoAcao){
    console.log('Usuário conectado')

    var url = '/att_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'produtoID':produtoID, 'produtoAcao': produtoAcao})
    })
    
    .then((response) => {
        return response.json()
    })
    
    .then((data) => {
        console.log('Dados:', data)
        location.reload()
    } )
}