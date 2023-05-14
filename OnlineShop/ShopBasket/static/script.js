$(document).ready(function(){
    $(".plus").click(function(){
        let amount = $(this).closest(".quantity").find("input").val();
        amount = parseInt(amount);
        amount = amount+1;
        $(this).closest(".quantity").find("input").val(`${amount}`)
    })

    $(".minus").click(function(){
        let amount = $(this).closest(".quantity").find("input").val();
        amount = parseInt(amount);
        if (amount-1 !== 0){
            amount = amount-1;
            $(this).closest(".quantity").find("input").val(`${amount}`)
        }
    })

    $(".add-basket").click(function(){
        $.ajax({
            url: $(".url-get-basket").val(),
            type: 'get',
            data: {
                pk: $(this).val(),
                method: 'add'
            },
        })
    })
    $(".del-basket").click(function(){
        $(this).closest(".product").remove();
        $.ajax({
            url: $(".url-get-basket").val(),
            type: 'get',
            data: {
                pk: $(this).val(),
                method: 'del'
            },
        })
    })

})