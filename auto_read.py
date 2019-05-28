import time

import requests
import datetime

url = "http://suda.wnssedu.com/course/Servlet/recordStudy.svl"

querystring = {"lCoursewareId": "319", "strStartTime": "1559052246825", "nCurSeconds": "0", "lNewCourseId": "69"}

headers = {
    'Cookie': "JSESSIONID=CB401E7941C1E71EA0A708807CF15EFE; UM_distinctid=16afe5ee044d75-0847daec99c0b7-e353165-1fa400-16afe5ee0456fd; accessId=4f7e0760-7dcc-11e8-8af2-156db96c823d; bad_id4f7e0760-7dcc-11e8-8af2-156db96c823d=7098fd91-8142-11e9-93e6-b97368d24386; href=http%3A%2F%2Fsuda.wnssedu.com%2F; nice_id4f7e0760-7dcc-11e8-8af2-156db96c823d=6f03d741-8145-11e9-93e6-b97368d24386; loginname=suda1605408026; luserid=31800000242; token=180315afe7bc1b567d67fa2776e114ab231b5aba1372fb64b0113a0bc5e32efd1939a8d681f4dde29c37f6df95db33c16d499911583fc4335238fc45f295237db9d2da42be1f12fddde210021b1b4cf9d32c6685b085eb0f; lasttime=1559047808429; schoolToken=180315afe7bc1b56c1d7e40653844d0af44ecc7556625f098685ff4483a7f1ef574fc07852f41ae6c58a3a449cad4ec446d556bfd3ea09ed0757dbe0bf6fe3f1d69a707879e5d28921b5d64348fe0b3fff6919dd5effa38cb6c69433d6e052b0848e21729c566b0932883366e73c4756048cc9e01669f60811564b1403e0ee1e7b4feae6fc199536; Courseware_3180000024248=8c9046cf06258c0ba352bc412baefbd509f1b52b8331f09bbc5106a29b45d538; Courseware_31800000242141=9c8cf40e5d6414bb8e9ec312763527b9d569067a5c5926e053ac09d5785a55b7; Courseware_3180000024257=8c9046cf06258c0b177e69f6bea923b1ce108bc081222a6a13facac6d3889da9; Courseware_31800000242211=9c8cf40e5d6414bbaf2377412d2d627db223a9857b2e320a191c8d9f424cc8f2; Courseware_31800000242314=8c9046cf06258c0bee2b86c8d01e5ca7202697b94618c6cd9e8fd6a1d83ada54; Courseware_3180000024253=9c8cf40e5d6414bb5250d7696d2f9b2f8faf39e30b8414f3606e65292eb54144; Courseware_3180000024249=abf8c4ec9334ddb6b64f1d0f680ae51a2cf07736264cb30b3de6f9ea933ab43a; Courseware_31800000242315=279184081da372b72d778ffbb9faabf9e0fd183160a0023f68c74464bbd7a528; Courseware_31800000242185=8c9046cf06258c0b9d51f29d58c3956af9e10f6beb4ccfd3757bcf6949d96fcb; Courseware_31800000242142=4a52e3114d243e91be321a8f4ca3cd966e7121a4794eebb7c40743cb4dafa5e0; Courseware_31800000242212=de3e59038e8f0fd307f8ffd7a4f5a20d47363e8aa6fcc09cdb4242e22330a144; Courseware_3180000024254=4a499afd1700dad0810512ed81584521998dc0f14642a6e2386677e6c3adf9cd; Courseware_3180000024268=8c9046cf06258c0b66c24863a50f2a17583d2f72b22d4e28a4cfd3de60ef12ef; Courseware_3180000024258=de3e59038e8f0fd37ad1fd0f5a55a56e0be08e9ed7a038a211249c62534fe038; Courseware_3180000024260=84a8a0a32091d87ec2623498a3e9941f2bc233849416e5830f2bc3c412dff06b; Courseware_31800000242213=290c61bfe1c583ab29ddde13a098bd7be662883ef7321905791a786996fc11d4; Courseware_31800000242316=6194a6e97b3ef33649fd667bd5dd29c9a4c56db09e1b5768228bb8fc8cd3e16d; Courseware_31800000242150=e60484396b43f7294b8bc77cafc0005203128858c77096793fa703f96fc81b23; qimo_seosource_4f7e0760-7dcc-11e8-8af2-156db96c823d=%E7%AB%99%E5%86%85; qimo_seokeywords_4f7e0760-7dcc-11e8-8af2-156db96c823d=; CNZZDATA1273463993=12000183-1559040711-%7C1559053412; Courseware_31800000242385=c7409cc1299fe5730184f3cf2c8db65c1be79d6c1740763fb69348a873e5dbdd; Courseware_31800000242143=284878adc2246b3f4c7471a8a641fdbed7e7feeef86091f4597c5b66ef3ecaf3; Courseware_31800000242317=55cf13cc08ac234d0eb49bf0d863fe63b359c57909260b84ee470d2038217cec; pageViewNum=44; Courseware_31800000242319=d017deee78cab44cdaca18e87cac2e1f; Courseware_3180000024259=8c9046cf06258c0b872360a927fc99948071cf98016bcc0cf0ca4783a9fcd4ce; JSESSIONID=4CB68955392D59F838F75C306DBC8D5D; Courseware_31800000242152=67edced31e53cbe322422c259f18918a77b67063c3e91e4bae14aee4d06ed74d; Courseware_31800000242153=67edced31e53cbe3356c91f1367625dff3b3706a45f1036c3a5cbfb275b80bc1; Courseware_3180000024261=e47a9a4d76763374a52e5a133c07571107a5552c07bb544225345992619c28a4; Courseware_31800000242154=67edced31e53cbe38109543f2ce4cfb8632e4a99075db8138aa70c65742b780d; Courseware_3180000024262=f99d4e27441759de3d9542933c1c13889610cd1b05dc154bd935e02ddcf2fca0; Courseware_31800000242151=9b7721dd888cfdfc8219a987dfd7b0e09610cd1b05dc154bcfcd41670368f638; Courseware_3180000024255=290c61bfe1c583abd68d85cc6805c27ae0a928ede93fb6923584f62469f014d0; Courseware_31800000242318=b316fe1d35f0528984a135bfa0c098ffe0a928ede93fb6928b2b8d9c59eb1191; Courseware_3180000024256=f99d4e27441759de106d8017c2e197fd3e94921c6142866b1030b1c2b51e855a",
    'cache-control': "no-cache",
    'Postman-Token': "ba189ad9-2cd0-4862-8dd5-b7509a6c7557"
}

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

dtime = datetime.datetime.now()
ans_time = int(time.mktime(dtime.timetuple()) * 1000)
querystring.__setitem__("strStartTime", "1559054982574")

total = 1057
index = 126
while index < total:
    querystring.__setitem__("nCurSeconds", str(index))
    index += 60
    print(querystring)
    res = requests.request("GET", url, headers=headers, params=querystring)
    time.sleep(1)
querystring.__setitem__("nCurSeconds", "1057")
requests.request("GET", url, headers=headers, params=querystring)