import React from 'react'
import MobileList from './MobileList.jsx'

// const book1 = [{
//     image: "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/n/q/h/-original-imahgfmzjj8gtqbc.jpeg?q=70",
//     title: "Redmi Note 12 Pro 5G (Dark Night, 128 GB)  (8 GB RAM)",
//     price: "16,999"
// }]
// const book2 = {
//     image: "https://rukminim2.flixcart.com/image/312/312/xif0q/tablet/r/k/q/-original-imahayyde8ugshtm.jpeg?q=70",
//     title: "Redmi Note 12 Pro 5G (Dark Night, 128 GB)  (8 GB RAM)",
//     price: "16,999"
// }

// const books = [
//     {
//         image: "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/n/q/h/-original-imahgfmzjj8gtqbc.jpeg?q=70",
//         title: "Redmi Note 12 Pro 5G (Dark Night, 128 GB)  (8 GB RAM)",
//         price: "16,999"
//     }, {
//         image: "https://rukminim2.flixcart.com/image/312/312/xif0q/tablet/r/k/q/-original-imahayyde8ugshtm.jpeg?q=70",
//         title: "Redmi Note 12 Pro 5G (Dark Night, 128 GB)  (8 GB RAM)",
//         price: "16,999"
//     }
// ]

import books from './books.json'

function Mobile() {

    return (
        <div>
            {books.map((ele) => {
                return <MobileList
                    image={ele.image}
                    title={ele.title}
                    price={ele.price} />
            })}


            {/* <MobileList
                image={books[0].image}
                title={books[0].title}
                price={books[0].price} />
            <MobileList
                image={book2.image}
                title={book2.title}
                price={book2.price} /> */}
        </div>
    )
}

export default Mobile