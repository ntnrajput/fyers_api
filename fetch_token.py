from fyers_apiv3 import fyersModel
import webbrowser

# User-specific details
client_id = "VE3CCLJZWA-100"    # Example: 'UABC123XYZ-100'
secret_key = "QEGA69PVUL"
redirect_uri = "https://www.google.com"  # Example: 'https://www.yourdomain.com/callback'
response_type = "code"  
grant_type = "authorization_code"  

auth_code= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiJWRTNDQ0xKWldBIiwidXVpZCI6ImQ1MzhlM2Q1ODcxYjRmODViZGEwZDRlMTMxNWVjNGY5IiwiaXBBZGRyIjoiIiwibm9uY2UiOiIiLCJzY29wZSI6IiIsImRpc3BsYXlfbmFtZSI6IlhUMDI2MjQiLCJvbXMiOiJLMSIsImhzbV9rZXkiOiI5YjViNjVmY2VmMzliNjJjZDlkZjBjZmU4YzhjYmRlMDk3ZDQxYmRkMGRlMmFiNWZlZjgwYWZjYyIsImlzRGRwaUVuYWJsZWQiOiJOIiwiaXNNdGZFbmFibGVkIjoiTiIsImF1ZCI6IltcImQ6MVwiLFwiZDoyXCIsXCJ4OjBcIixcIng6MVwiLFwieDoyXCJdIiwiZXhwIjoxNzUxMjg1NDQyLCJpYXQiOjE3NTEyNTU0NDIsImlzcyI6ImFwaS5sb2dpbi5meWVycy5pbiIsIm5iZiI6MTc1MTI1NTQ0Miwic3ViIjoiYXV0aF9jb2RlIn0.uwJ3hp2fI8YQnZv0tWhR2z-3iU2Fp_EPxqCp4xZB3y4"

session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type=grant_type
)

session.set_token(auth_code)
response = session.generate_token()

print(response)