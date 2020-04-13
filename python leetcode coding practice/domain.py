
exa = ["9001 discuss.leetcode.com"]

def subdomainVisits(cpdomains):
    count = {}
    for domain in cpdomains:
        pair = domain.split()
        domainParts = pair[1].split(".")
        for i in range(len(domainParts)):
            webDomain = ".".join(domainParts[i:])
            count[webDomain] = count.get(webDomain,0) + int(pair[0])
    return [str(count[key]) + " "+ key for key in count]


A=[1,1,2,3,4]
B=[1,2,3,4,7]
def findLength(A, B):
        memo = [[0] * (len(B)) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    try:
                        memo[i][j] = memo[i-1][j-1]+1
                    except:
                        memo[i][j] = 1
        return max(max(row) for row in memo)
print(findLength(A,B))


completed_purchase_user_ids = [
  "3123122444","234111110", "8321125440", "99911063"]

ad_clicks = [
    ##userID, time, product
 "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
  "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
  "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
  "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
  "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
  "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

all_user_ips = [
  ##"User_ID,IP_Address",
   "2339985511,122.121.0.250",
  "234111110,122.121.0.1",
  "3123122444,92.130.6.145",
  "39471289472,96.3.199.11",
  "8321125440,82.1.106.8",
  "99911063,92.130.6.144"
]

##dic1 =  {ipAddress:userID}
##dic2 = {product:[totalClickTimes, purchasedTime]}

def task3(completed_purchase_user_ids,ad_clicks,all_user_ips):
    ipToId = {}
    productInfo = {}
    completed_purchase_user_ids = set(completed_purchase_user_ids)
    for info in all_user_ips:
        userId,ip = info.split(",")
        ipToId[ip]=userId
    for info in ad_clicks:
        ip,_,product = info.split(",")
        if product not in productInfo:
            productInfo[product] = [1,0]
        else:
            productInfo[product][0]+=1
        if ipToId[ip] in completed_purchase_user_ids:
            productInfo[product][1]+=1
    return productInfo
print(task3(completed_purchase_user_ids,ad_clicks,all_user_ips))
