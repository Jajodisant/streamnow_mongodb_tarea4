mongodb://localhost:27017/StreamNowDB

db.usuarios.find({ suscripcion: "premium", ciudad: "Medellín" })

db.usuarios.find()


db.usuarios.updateOne(
  { user_id: "U001" },
  { $set: { suscripcion: "standard" } })


db.historial_reproduccion.find({
  play_duration_min: { $gt: 60 }})

db.contenido.find({ etiquetas: "drama" })


db.historial_reproduccion.aggregate([
  { $group: { _id: "$content_id", total_views: { $sum: 1 } } },
  { $sort: { total_views: -1 } }, { $limit: 10 }])


db.historial_reproduccion.aggregate([
   { $group: { _id: "$user_id", total_minutes: { $sum: "$play_duration_min" } } },
   { $sort: { total_minutes: -1 } },
   { $limit: 10 }])


db.historial_reproduccion.aggregate([
   { $group: { _id: "$content_id", avg_duration: { $avg: "$play_duration_min" } } },
   { $sort: { avg_duration: -1 } }])



  db.historial_reproduccion.aggregate([
  {
    $lookup: {
      from: "dispositivos",
      localField: "device_id",
      foreignField: "device_id",
      as: "device"
    }
  },
  { $unwind: "$device" },
  { $group: { _id: "$device.tipo", count: { $sum: 1 } } },
  { $sort: { count: -1 } }])

