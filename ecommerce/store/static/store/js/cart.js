var attbotao = document.getElementsByClassName("att-cart")

for(var i = 0; i < attbotao.length; i++){
    attbotao[i].addEventListener("click", function(){
        var produtoId = this.dataset.produto
        var produtoAcao = this.dataset.acao 
        console.log('produtoID:',produtoId, 'produtoAcao:',produtoAcao)

        if(user === 'AnonymousUser'){
            console.log('Não está logado')
        }else{
            attPedidoUser(produtoId, produtoAcao)
        }
    })
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