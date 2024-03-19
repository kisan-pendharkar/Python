from fastapi import FastAPI
import uvicorn
import base64
app=FastAPI( description="This is simple encryption and decryption API's")

result={}

@app.get("/encrypt{var}", tags=['encryption'] ,summary="Encrypt an string")
async def Encrypt_value(var:str):
	try:
		data=var
		new_data = base64.b64encode(data.encode("ascii"))
		
		result['data']=new_data
		result['message']="String Encryption successful."
		result['success']=True
		return result
	except Exception as e:
		result['data']=""
		result['message']="String Encryption unsuccessful. :"+str(e)
		result['success']=False
		return result
		

@app.get("/decrypt{var}",tags=['decryption'],summary="Decrypt an string")
async def decrypt_value(var:str):
	try:
		data=var
		new_data = base64.b64decode(data.encode("ascii"))
		result={}
		result['data']=new_data
		result['message']="String decryption successful."
		result['success']=True
		return result
	except Exception as e:
		result['data']=""
		result['message']="String decryption unsuccessful. :"+str(e)
		result['success']=False
		return result

if __name__ == "__main__":
   uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
