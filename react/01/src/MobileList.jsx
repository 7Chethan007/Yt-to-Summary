import React from 'react'
import './MobileList.css'


const MobileList = (props) => {
    const {image, title, price} = props;

        return (
        <div className='main'>
            {console.log(props)}
            <img className='image'
             src={image} alt="" />
            <div>
             <h3>{title}</h3>
             <h4>₹{price}</h4>
            <button>Add to Cart</button>
            </div>
        </div>
    )
    
    // return (
    //     <div className='main'>
    //         {console.log(props)}
    //         <img className='image'
    //          src={props.image} alt="" />
    //         <div>
    //          <h3>{props.title}</h3>
    //          <h4>₹{props.price}</h4>
    //         <button>Add to Cart</button>
    //         </div>
    //     </div>
    // )
}

export default MobileList