/**
 * Author: Mahad Osman  
 * Date: Jan 31, 2023
 * Assignment: Flask cupcakes
 */

const URL = "http://127.0.0.1:5000/api";
const $cupcakelist = $("#cupcake_list")
const $cupcakeform = $("#cupcake_form")



/**
 * A function to take in cupcakedata and return an html representation of it
 * @param {*} cupcakedata 
 */
function createCupCakes(cupcakedata){
    return `
    <div data-id = ${cupcakedata.id}> 
        <li>
            Flavor: ${cupcakedata.flavor}, Size: ${cupcakedata.size}, Rating:${cupcakedata.rating}
            <button class= "btn btn-danger btn-small"> delete</button>

        </li>
        <img src = ${cupcakedata.image} width = 200px height= 200px
        alt = "(No image)">        
    </div>
    `
}



async function retrievecupcakes(){
    // const response = await axios.get("http://127.0.0.1:5000/api/cupcakes")
    const response = await axios.get(`${URL}/cupcakes`)
    // console.log(response)
    for(let cupcake of response.data.cupcakes){
        let newCupcake = $(createCupCakes(cupcake));
        $cupcakelist.append(newCupcake)
    }
}


// Our form submission handler 
$cupcakeform.on("submit", async function(evt) {
    evt.preventDefault();

    //Pulling the values from out form inputs
    let flavor = $("#flavor").val()
    let rating = $("#rating").val()
    let size = $("#size").val()
    let image = $("#image").val()

    const newCupCakeRes = await axios.post(`${URL}/cupcakes`, {
        flavor,
        rating,
        size,
        image
    });

    //once posted to our api we will create the html element and post it to the front end
    let newCupcake = $(createCupCakes(newCupCakeRes.data.cupcake))
    $cupcakelist.append(newCupcake)
    $(retrievecupcakes);
})

/** handling our delete */
$cupcakelist.on("click", "button", async function(evt){
    evt.preventDefault();
    //console.log("Inside the delete")

    let cupcake = $(evt.target).closest("div");
    let deletionId = cupcake.attr("data-id")
    //console.log(deletionId)

    //Now to delete the cupcake via the ID
    await axios.delete(`${URL}/cupcakes/${deletionId}`)
    //And to remove it from our DOM
    cupcake.remove();
})

//Loads in our cupcake list!
$(retrievecupcakes);