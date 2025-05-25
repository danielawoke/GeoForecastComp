import Image from "next/image";

export default function Home() {
  return (
    <div className="w-150 h-screen flex flex-col m-auto">
      <div>
        <div className="mt-10 font-[impact] text-5xl text-black w-150 drop-shadow-[0_0px_3px_rgba(255,255,255,1)] m-auto">
          Paste or upload your data
        </div>
        <textarea className="text-black mt-10 w-150" style={{backgroundColor: 'rgba(255, 255, 255, 0.94)'}}></textarea>
      </div>
    </div>
  );
}
