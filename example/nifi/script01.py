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
            count = 0
            while (count <= 59):
                detester = input_obj['create_time']
                date = (datetime.datetime.strptime(detester, '%Y-%m-%d %H:%M:%S.%f') + datetime.timedelta(
                    minutes=count))
                output_obj = {
                    "id": input_obj['id'],
                    "meas_type": input_obj['meas_type'],
                    "create_time": date.strftime("%Y-%m-%d %H:%M:%S.%f"),
                    "create_day": datetime.datetime.strptime(date.strftime("%Y-%m-%d"), '%Y-%m-%d').strftime(
                        "%Y-%m-%d %H:%M:%S.%f"),
                    "create_minute": date.strftime("%H:%M:%S.%f")
                }
                if count == 0:
                    output_obj['vtype'] = '时间'
                elif count == 1:
                    output_obj['vtype'] = '最大值'
                elif count == 2:
                    output_obj['vtype'] = '最小值'
                else:
                    output_obj['vtype'] = '平均值'

                if count < 10:
                    objkey = 'v0' + str(count)
                    if input_obj[objkey] is None:
                        output_obj['val'] = 0
                    else:
                        output_obj['val'] = input_obj[objkey]
                else:
                    objkey = 'v' + str(count)
                    if input_obj[objkey] is None:
                        output_obj['val'] = 0
                    else:
                        output_obj['val'] = input_obj[objkey]
                # Write output content
                output_arr.append(output_obj)
                count = count + 1
            output_text = json.dumps(output_arr)
            outputStream.write(StringUtil.toBytes(output_text))

        except:
            traceback.print_exc(file=sys.stdout)
            raise


flowFile = session.get()
if flowFile != None:
    flowFile = session.write(flowFile, TransformCallback())
    # Finish by transferring the FlowFile to an output relationship
    session.transfer(flowFile, REL_SUCCESS)
