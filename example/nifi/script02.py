import json
import sys
import traceback
import datetime
from java.nio.charset import StandardCharsets
from org.apache.commons.io import IOUtils
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil


class TransformCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        try:
            # Read input FlowFile content
            input_text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
            input_obj = json.loads(input_text)

            # Transform content
            # for i in range(0, len(input_obj)):
            output_arr = []

            # detester = '2018-04-12 00:00:00.0'

            detester = input_obj['create_time']
            #starttime = detester
            #endtime = datetime.datetime.strptime(detester, '%Y-%m-%d %H:%M:%S.%f') + datetime.timedelta(days=1)
            # '2018-04-09 00:00:00.0'
            # detesterend = '2018-04-12 00:00:00.0'
            # ids \
            id = input_obj['id']
            # ['130199010600000501', '130199010600000502']
            # input_obj['id']
            # meas_types
            meas_type = input_obj['meas_type']
            # ['1001', '3101']
            # input_obj['meas_type']
            # for id in ids:
            # for meas_type in meas_types:
            # for k in range(0, 38):
            for i in range(0, 24):
                for j in range(0, 60):
                    date = datetime.datetime.strptime(detester, '%Y-%m-%d %H:%M:%S.%f') + datetime.timedelta(
                        hours=i) + datetime.timedelta(minutes=j)
                    output_obj = {
                        "id": id,
                        "meas_type": meas_type,
                        "val": 0,
                        "create_time": date.strftime("%Y-%m-%d %H:%M:%S.%f"),
                        "create_day": datetime.datetime.strptime(date.strftime("%Y-%m-%d"),
                                                                 '%Y-%m-%d').strftime(
                            "%Y-%m-%d %H:%M:%S.%f"),
                        "create_minute": date.strftime("%H:%M:%S.%f")
                    }
                    if j == 0:
                        output_obj['vtype'] = '时间'
                    elif j == 1:
                        output_obj['vtype'] = '最大值'
                    elif j == 2:
                        output_obj['vtype'] = '最小值'
                    else:
                        output_obj['vtype'] = '平均值'
                    # Write output content
                    output_arr.append(output_obj)
            output_text = json.dumps(output_arr)
            outputStream.write(StringUtil.toBytes(output_text))

        except:
            traceback.print_exc(file=sys.stdout)
            raise


#flowFile = session.create()
flowFile = session.get()
if flowFile != None:
    flowFile = session.write(flowFile, TransformCallback())
    # Finish by transferring the FlowFile to an output relationship
    session.transfer(flowFile, REL_SUCCESS)
