'use client'

import Image from "next/image";
import React, { useRef } from 'react';

export default function Home() {
  const textArea = useRef(null);
  
  async function f(){
    let data = textArea.current.value
    const url = 'http://127.0.0.1:8000/postRequest/';

    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
                              "name":"stevie Wozinakerson"
                          }),
                        })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((responseData) => {
        console.log('Success:', responseData);
      })
      .catch((error) => {
        console.error('Error:', error);
      });

  }

  

  return (
    <div className="w-150 h-screen flex flex-col m-auto">
      <div>
        <div className="mt-10 font-[impact] text-5xl text-black w-150 drop-shadow-[0_0px_3px_rgba(255,255,255,1)] m-auto">
          Paste or upload your data
        </div>
        <textarea className="text-black mt-10 w-150" style={{backgroundColor: 'rgba(255, 255, 255, 0.94)'}} ref={textArea} />
         <button onClick={f} type="button">Click Me!</button> 
      </div>
    </div>
  );
}
