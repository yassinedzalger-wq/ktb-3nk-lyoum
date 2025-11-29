export default function Home() {
  return (
    <div style={{padding: "40px", textAlign: "center", fontFamily: "Tajawal, Arial"}}>
      <h1 style={{fontSize: "52px", color: "#006233", marginBottom: "10px"}}>
        كتب عنك اليوم
      </h1>
      <p style={{fontSize: "28px", color: "#333", marginBottom: "40px"}}>
        اعرف ماذا كُتب عن شركتك أو اسمك في كل الأخبار الجزائرية والعربية اليوم
      </p>
      
      <div style={{margin: "40px auto", maxWidth: "600px"}}>
        <input 
          type="text" 
          placeholder="اسم الشركة أو الشخص (سوناطراك، كوندور، سيفيتال...)" 
          style={{width: "100%", padding: "18px", fontSize: "22px", borderRadius: "12px", border: "2px solid #006233"}}
        />
        <button style={{marginTop: "20px", padding: "18px 50px", fontSize: "24px", background: "#006233", color: "white", border: "none", borderRadius: "12px"}}>
          ابحث الآن
        </button>
      </div>

      <p style={{marginTop: "60px", fontSize: "20px", color: "#555"}}>
        النسخة التجريبية مجانية 100% لأول 500 مستخدم جزائري
      </p>
    </div>
  )
}
